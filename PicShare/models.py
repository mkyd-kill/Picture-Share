from datetime import datetime
from flask_login import UserMixin
from . import db

class Users(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, db.Sequence('user_id_seq'), primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String, nullable=False)
    profile_pic = db.Column(db.String, nullable=True)
    date_registered = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    authenticated = db.Column(db.Boolean, default=False)

    def is_active(self):
        """ returns True for all active users"""
        return True
    
    def get_id(self):
        """ return the email address to satisfy flask-login's requirement"""
        return self.id

    def is_authenticated(self):
        """ Return true is user is authenticated """
        return self.authenticated

    def is_anonymous(self):
        """ return false as anonymous users are not supported"""
        return True

    def __repr__(self) -> str:
        return "<User(username='%s', email='%s', password='%s')>" % (self.username, self.email, self.password)

    def serialize(self):
        """ needed when returning user objects in response to JSON """
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'password': self.password
        }

# for the messages
class Messages(db.Model):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    senders_username = db.Column(db.String, nullable=False) # username of the sender
    senders_message = db.Column(db.String, nullable=True) # message of the sender
    sent_date = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)  # date of the message sent

    def __repr__(self) -> str:
        return "<Message(username='%s', message='%s', dateSent='%s')>" % (self.senders_username, self.senders_message, self.sent_date)

# for the comments
class Comments(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    commenter = db.Column(db.String, nullable=False)
    comment_msg = db.Column(db.String, nullable=False)
    comment_date = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)