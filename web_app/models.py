#from web_app import db
from web_app import db
from datetime import datetime

class User(db.Model):
    # add columns
    id = db.Column(db.Integer , primary_key = True)
    username = db.Column(db.String(20) , unique = True , nullable = True)
    email = db.Column(db.String(120) , unique = True , nullable = True)
    image_file = db.Column(db.String(20) , nullable = False , default = 'default.jpg' ) # we hash the image files to strings #profile pic
    password = db.Column(db.String(60) , nullable = False ) # hashing passwords to 60 char length
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    title = db.Column(db.String(120) , nullable = False )
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
