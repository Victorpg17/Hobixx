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
            confirm = request.form['confirm_password']

            if password != confirm:
                return render_template('index.html', mensaje="Las contraseñas no coinciden")

            hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')
            resultado = insertUser(name, email, hashed_pw)

            if resultado == 'existe':
                return render_template('index.html', mensaje="Este correo ya está registrado")
            else:
                return render_template('index.html', mensaje="Registro exitoso. Ahora inicia sesión.")

        elif action == 'login':
            email = request.form['email']
            password_in = request.form['password']
            
            usuario = getUser(email)

            if not usuario:
                return render_template('index.html', mensaje="Usuario no registrado")

            if bcrypt.check_password_hash(usuario['password'], password_in):
                session['user_id'] = str(usuario['_id'])
                session['username'] = usuario['name']
                return redirect(url_for('home'))
            else:
                return render_template('index.html', mensaje="Contraseña incorrecta")

    return render_template('index.html')

@app.route('/home')
def home():
    if 'user_id' not in session:
        return redirect(url_for('index'))

    hobbies = getAllHobbies(session['user_id'])
    return render_template('home.html', hobbies=hobbies, username=session['username'])

@app.route('/hobbies')
def add_hobbie():
    hobbie = request.form['hobbie']
    info = request.form['info']
    percentage = request.form['percentage']
    


if __name__ == '__main__':
    app.run(debug=True)