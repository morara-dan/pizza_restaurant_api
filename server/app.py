from flask import Flask, jsonify, request

from server import db, migrate
from server.config import Config
from server import models
from server.controllers.restaurant_controller import get_restaurants, get_restaurant_by_id, delete_restaurant
from server.controllers.pizza_controller import get_pizzas
from server.controllers.restaurant_pizza_controller import create_restaurant_pizza

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
    if status_code == 404:
         return jsonify(restaurant_data), status_code
    return jsonify(restaurant_data), status_code

@app.route('/restaurants/<int:id>', methods=['DELETE'])
def remove_restaurant(id):
    message, status_code = delete_restaurant(id)
    if status_code == 204:
        return '', 204
    else:
        return jsonify(message), status_code

@app.route('/pizzas', methods=['GET'])
def list_pizzas():
    pizzas_data = get_pizzas()
    return jsonify(pizzas_data), 200

@app.route('/restaurant_pizzas', methods=['POST'])
def add_restaurant_pizza():
    data = request.get_json()
    response_data, status_code = create_restaurant_pizza(data)
    return jsonify(response_data), status_code

if __name__ == '__main__':
    app.run(debug=True, port=5555)