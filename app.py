from flask import Flask, render_template, request, redirect, url_for, session
from hobbie import Hobbie, insertHobbie, getAllHobbies
from user import User, insertUser, getUser
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.secret_key = '12345'
bcrypt = Bcrypt(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        action = request.form['action']

        if action == 'register':
            name = request.form['name']
            email = request.form['email']
            password = request.form['password']

            hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')

            user = User(name, email, hashed_pw)
            resultado = insertUser(user)

            if resultado == 'existe':
                return render_template('index.html', mensaje="Este correo ya está registrado")
            else:
                return render_template('index.html', mensaje="Registro exitoso. Ahora inicia sesión.")

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
    print(session)
    print(hobbies)
    return render_template('home.html', hobbies=hobbies, username=session['username'])

@app.route('/hobbies')
def add_hobbie():
    name = request.form['hobbie']
    info = request.form['info']
    percentage = request.form['percentage']
    
    if name and info and percentage:
        hobbie = Hobbie(name, info, percentage)
        hobbie.user_id = session['user_id']

        insertHobbie(hobbie)

if __name__ == '__main__':
    app.run(debug=True)