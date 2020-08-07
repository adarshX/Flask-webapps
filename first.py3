from flask import Flask 
import datetime  
from flask import render_template 
app = Flask(__name__)

@app.route("/")  
def index(): 
    return render_template("index.html")

if __name__ == "__main__":
    app.run()



