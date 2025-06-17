from server import db
from server.models import Restaurant, RestaurantPizza

def get_restaurants():
    restaurants = Restaurant.query.all()
    return [r.to_dict() for r in restaurants]

def get_restaurant_by_id(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)

    if not restaurant:
        # Restaurant not found
        return {"error": "Restaurant not found"}, 404
    else:
        # Restaurant found, return its data including pizzas
        return restaurant.to_dict_with_pizzas(), 200

# Future function for DELETE /restaurants/<id> will go here