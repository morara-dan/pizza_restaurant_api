from flask import Flask, jsonify, request

from server import db, migrate
from server.config import Config
from server import models
from server.controllers.restaurant_controller import get_restaurants, get_restaurant_by_id # Added get_restaurant_by_id

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app, db)

@app.route('/')
def home():
    return jsonify(message="Welcome to the Pizza Restaurant API!")

@app.route('/restaurants', methods=['GET'])
def list_restaurants():
    restaurants_data = get_restaurants()
    return jsonify(restaurants_data), 200

@app.route('/restaurants/<int:id>', methods=['GET'])
def show_restaurant(id):
    restaurant_data, status_code = get_restaurant_by_id(id)
    return jsonify(restaurant_data), status_code

if __name__ == '__main__':
    app.run(debug=True, port=5555)