from flask import Flask, jsonify
from routes.users import users_bp
from setup import init_db

init_db()

app = Flask(__name__)
app.register_blueprint(users_bp)


@app.route('/')
def hello_world(): 
    return jsonify({ "status": "success", "message": "Hello World!" }), 200


if __name__ == '__main__':
  app.run(host="0.0.0.0", port=5000)
