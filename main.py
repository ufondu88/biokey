from flask import Flask, jsonify
from routes.users import users_bp
from setup import Base, engine


app = Flask(__name__)
app.register_blueprint(users_bp)

def init_db():
  Base.metadata.create_all(bind=engine)


@app.route('/')
def hello_world(): 
    return jsonify({ "status": "success", "message": "Hello World!" }), 200


if __name__ == '__main__':
  init_db()

  app.run(host="0.0.0.0", port=3000)