from flask import Blueprint, render_template

view = Blueprint(
    'views',
    __name__,
    url_prefix='/'
)

# AIM: to deal with the home page and picture view

@view.route('/picture-details')
def home():
    return render_template('index.html')