from flask import Flask, render_template
from flask_sslify import SSLify
from flask_socketio import SocketIO
from os import environ, path

socketio = SocketIO()

def create_app():
    app = Flask(
        __name__,
        instance_relative_config=True,
        static_url_path='/static'
    )
    sslify = SSLify(app)
    socketio.init_app(app)

    # blueprint registeration
    from .admin import admin
    from .auth import auth
    from .dash import dashboard
    from .views import view

    app.register_blueprint(admin)
    app.register_blueprint(auth)
    app.register_blueprint(dashboard)
    app.register_blueprint(view)

    # check if the app is running on heroku
    if 'DYNO' in environ:
        sslify = SSLify(app)

    """
    Custom URL page errors
    """
    # Bad Request
    @app.errorhandler(400)
    def page_not_found(e):
        return render_template("400.html"), 400

    # Unauthorized access
    @app.errorhandler(401)
    def page_not_found(e):
        return render_template('401.html'), 401

    # Forbidden URL only admin accessible
    @app.errorhandler(403)
    def page_not_found(e):
        return render_template("403.html"), 403

    # Invalid URL input
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("404.html"), 404

    # Method not allowed
    @app.errorhandler(405)
    def page_not_found(e):
        return render_template('405.html'), 405

    # request time out
    @app.errorhandler(408)
    def page_not_found(e):
        return render_template('408.html'), 408

    # Internal Server Error
    @app.errorhandler(500)
    def page_not_found(e):
        return render_template('500.html'), 500

    # Bad Gateway connection
    @app.errorhandler(502)
    def page_not_found(e):
        return render_template('502.html'), 502

    # Gateway connection timeout
    @app.errorhandler(504)
    def page_not_found(e):
        return render_template('504.html'), 504

    # after request handler
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET, PUT, POST, DELETE')
        return response

    # creating the database
    create_database()

    return app

DB_NAME = 'DATABASE.db'
def create_database():
    from .modules import Base, engine
    if not path.exists('PicShare/database/' + DB_NAME):
        Base.metadata.create_all(engine)
        print('DataBase Created Successfully!')