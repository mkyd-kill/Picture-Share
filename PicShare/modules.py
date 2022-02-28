from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column, create_engine, Sequence, DateTime, Boolean
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///PicShare/DATABASE.db", echo=True)

Base = declarative_base()
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, unique=True)
    password = Column(String, nullable=False)
    profile_pic = Column(String, nullable=False)
    date_registered = Column(DateTime(timezone=True), default=datetime.utcnow)
    authenticated = Column(Boolean, default=False)

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
class Messages(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True)
    senders_username = Column(String, nullable=False) # username of the sender
    senders_message = Column(String, nullable=True) # message of the sender
    sent_date = Column(DateTime(timezone=True), default=datetime.utcnow)  # date of the message sent

    def __repr__(self) -> str:
        return "<Message(username='%s', message='%s', dateSent='%s')>" % (self.senders_username, self.senders_message, self.sent_date)

