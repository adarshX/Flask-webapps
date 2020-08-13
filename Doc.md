# Documentation - Webapp

### Step 1 : Setup in local machine
* Create a virutal environment in your local machine
* Install all required packages  (refer requirements.txt)
<br>

### Step 2 : Creating Flask app
* Create a basic **blog posts** webapp using flask
* First create a `run.py` file which is main file to run the app
* Then create `HTML` files for , home , login and signup pages.
* Style the pages using  CSS (main.css) and layout.html(main template) 
* Add all required features (login , forms etc) in respective python files using flask.
* create a `SQLite3` database using flask-SQLAlchemy to store the data of users.
* Create a **package**` of all these files except run.py.
* Name the package with the name of webapp and intialise the package with "__init.py__"
<br>

### Step 3 : Testing the webapp 
* we can  test the app locally using local host
* Just run the main file `run.py` which creates the environment variable automatically and runs the webapp on the loclahost
* open `http://localhost:5000/` to check your webapp and its features
<br>

### Step 4 : Deploying on heroku
* Create a `requirements.txt` file which includes all the packages required to run the webapp on any machine
* Also include the python version in a runtime.txt file
* Create a `Procfile` which only contains **web: gunicorn FILE_NAME:APP_NAME**
* Now deploy the app using basic commands of `Heroku CLI`.
<br>


### References:
1) [Creating Virtual environments](https://www.youtube.com/watch?v=UqkT2Ml9beg)
2) **Creating Flask webapp and adding features** :   [videos]() &nbsp;&nbsp;  [github](https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Flask_Blog)
3) **Heroku CLI Documentation** :  [Basic](https://devcenter.heroku.com/articles/getting-started-with-python) &nbsp;&nbsp;  [CLI Commands](https://devcenter.heroku.com/articles/heroku-cli-commands) 
