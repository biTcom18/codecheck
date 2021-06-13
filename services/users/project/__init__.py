from flask import Flask, jsonify

app = Flask(__name__)

app.config.from_object('project.config.DevelopmentConfig')

@app.route('/')
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })

