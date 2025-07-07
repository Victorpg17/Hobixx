from flask import Flask, render_template, request, redirect, url_for, session
from hobbie import Hobbie, insertHobbie, getAllHobbies
from user import User, insertUser, getUser
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.secret_key = '12345'
bcrypt = Bcrypt(app)

# LOGIN/REGISTER FORMS PAGE
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        action = request.form['action']

        # REGISTER FORM 
        if action == 'register':
            name = request.form['name']
            email = request.form['email']
            password = request.form['password']

            hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')

            # ADD USER IN THE DATABASE
            user = User(name, email, hashed_pw)
            newUser = insertUser(user)

            # CHECK IF IT EXISTS
            if newUser == 'exists':
                return render_template('index.html', mensaje="Este correo ya está registrado")
            else:
                return render_template('index.html', mensaje="Registro exitoso. Ahora inicia sesión.")

        # LOGIN FORM
        elif action == 'login':
            email = request.form['email']
            password_in = request.form['password']
            
            user = getUser(email)

            if not user:
                return render_template('index.html', mensaje="Usuario no registrado")

            if bcrypt.check_password_hash(user['password'], password_in):
                session['user_id'] = str(user['_id'])
                session['username'] = user['name']
                return redirect(url_for('home'))
            else:
                return render_template('index.html', mensaje="Contraseña incorrecta")

    return render_template('index.html')

@app.route('/home')
def home():
    if 'user_id' not in session:
        return redirect(url_for('index'))

    hobbies = getAllHobbies(session['user_id'])

    for hobbie in hobbies:
        hours = int(hobbie.get('hours', 0))
        minutes = int(hobbie.get('minutes', 0))
        totalMinutes = hours * 60 + minutes
        percentage = round((totalMinutes / 1440) * 100, 2)
        hobbie['percentage'] = percentage

    return render_template('home.html', hobbies=hobbies, username=session['username'])

@app.route('/hobbies', methods=['POST'])
def addHobbie():
    name = request.form['hobbie']
    info = request.form['info']
    hours = request.form['hours']
    minutes = request.form['minutes']

    if hours == '':
        hours = '0'

    if minutes == '':
        minutes = '0'
    
    if name and info and hours and minutes:
        user_id = session['user_id']
        hobbie = Hobbie(user_id, name, info, hours, minutes)

        insertHobbie(hobbie)

    return redirect(url_for('home'))

@app.route('/signOut')
def signOut():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)