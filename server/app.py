from flask import Flask, jsonify
from server import db, migrate
from server.config import Config


app = Flask(__name__)

# Load configurations from our Config class (e.g., SQLALCHEMY_DATABASE_URI)
app.config.from_object(Config)

db.init_app(app)

migrate.init_app(app, db)


@app.route('/')
def home():
    """
    Returns a simple success message indicating the server is running.
    """
    return jsonify(message="Welcome to the Pizza Restaurant API!")


if __name__ == '__main__':
    # debug=True enables reloader and debugger for easier development
    # port=5555 is a common alternative port to avoid conflicts
    app.run(debug=True, port=5555)