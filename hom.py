from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from data import Articles

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html')
 
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles')
def article():
    return render_template('articles.html', article = Articles) 

class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=40)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=10, max=25)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message = "Passwords don't match")
    ])
    confirm = PasswordField('Confirm Password')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method=='POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt (str(form.password.data))

    return render_template('register.html', form=form)

if __name__=='__main__':
    app.secret_key = 'secret123'
    app.run(debug=True)