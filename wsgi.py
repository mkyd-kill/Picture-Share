from PicShare import create_app, socketio

app = create_app()

if __name__ == '__main__':
    #socketio.run(app, debug=True, host='0.0.0.0', port=5004)
    app.run(debug=True, port=5004)