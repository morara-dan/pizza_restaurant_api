from server import db
from server.models import Restaurant, RestaurantPizza

def get_restaurants():
    restaurants = Restaurant.query.all()
    return [r.to_dict() for r in restaurants]

def get_restaurant_by_id(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)
    if not restaurant:
        return {"error": "Restaurant not found"}, 404
    else:
        return restaurant.to_dict_with_pizzas(), 200

def delete_restaurant(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)
    if not restaurant:
        return {"error": "Restaurant not found"}, 404
    else:
        db.session.delete(restaurant) 
        db.session.commit()          

        
        return {}, 204