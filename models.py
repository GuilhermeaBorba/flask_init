from flask_init import db

class Login(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(80))
    email = db.Column(db.String(35), unique=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))
    is_pessoa = db.Column(db.Boolean)

    def __init__(self, fullname, email, username, password, is_pessoa=False):
        self.fullname = fullname
        self.email = email
        self.username = username
        self.password = password
        self.is_pessoa = is_pessoa

    def __repr__(self):
        return '<Login %r>' % self.username
