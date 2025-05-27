from flask import Flask, render_template, request, redirect, url_for
from hobbie import insertHobbie, getAllHobbies

app = Flask(__name__)

@app.route('/')
def home():
    hobbies = getAllHobbies()
    return render_template('index.html', hobbies=hobbies)

@app.route('/hobbies')
def add_hobbie():
    hobbie = request.form['hobbie']
    info = request.form['info']
    percentage = request.form['percentage']
    


if __name__ == '__main__':
    app.run(debug=True)