from flask import Flask
from flask import flash, redirect, render_template, request, session, abort , url_for
from web_app.forms import RegisterForm , LoginForm
from web_app.models import User , Post
from web_app import app

details = [
    {
        'author': 'Adarsh BANDI',
        'title': 'Flask blogs',
        'content':'How to use flask',
        'date_posted': 'Aug 8 , 2020'
    }
    ,
    {
        'author': 'Ady',
        'title': 'Movie blogs',
        'content': ' Maniratnam cinemas',
        'date_posted': 'Aug 7 , 2020'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",  details = details)

@app.route("/about" , )
def about():
    return render_template("about.html", title = 'Details')


@app.route("/regsiter" ,   methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))

    return render_template('register.html' , title = 'Register', form = form)


@app.route("/Login" ,  methods=['GET', 'POST'])
def Login():
    form = LoginForm()
    if form.validate_on_submit():

        ## lets create a temporary check till we have a datbase created
        if form.email.data == 'adarshbandi8@gmail.com' and form.password.data == 'Adarsh@123' :
            flash('Login Succesfull !', 'success')
            return redirect(url_for('home'))
        else :
            flash('Login Unsuccessful. Either Invalid login credentials or Create an account', 'danger')
    return render_template('login.html' , title = 'Login', form = form)
