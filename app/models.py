
from .extensions import db  # This line is crucial for finding the db instance
from flask_login import UserMixin

class Item(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    owner = db.Column(db.Integer, db.ForeignKey('user.id'))
    owner_rel = db.relationship('User', back_populates='items')


# A user of the app
class User (db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(length  = 30), nullable = False, unique = True)
    email_id = db.Column(db.String(length = 69), nullable = False, unique = True)
    password = db.Column(db.String(length = 100), nullable = False)
    profile_pic = db.Column(db.String(length = 100), nullable = True, default = 'default.jpg')
    # Use back_populates for a clearer relationship definition
    items = db.relationship('Item', back_populates='owner_rel', lazy = True)

    def check_password_correction(self, attempted_password):
        return self.password == attempted_password



