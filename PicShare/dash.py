from flask import Blueprint
from flask_socketio import emit, send
from . import socketio

dashboard = Blueprint(
    'dash',
    __name__,
    url_prefix='/'
)

# AIM: to deal with message between users