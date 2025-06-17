from server import db
from server.models import Restaurant, Pizza, RestaurantPizza

def create_restaurant_pizza(data):
    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    if price is None or pizza_id is None or restaurant_id is None:
         return {"errors": ["Missing required data (price, pizza_id, or restaurant_id)"]}, 400

    pizza = Pizza.query.get(pizza_id)
    restaurant = Restaurant.query.get(restaurant_id)

    if not pizza or not restaurant:
         error_messages = []
         if not pizza:
              error_messages.append(f"Pizza with id {pizza_id} not found.")
         if not restaurant:
               error_messages.append(f"Restaurant with id {restaurant_id} not found.")
         return {"errors": error_messages}, 404

    try:
        new_rp = RestaurantPizza(
            price=price,
            pizza=pizza,
            restaurant=restaurant
        )

        db.session.add(new_rp)
        db.session.commit()

        return new_rp.to_dict_full(), 201

    except ValueError as e:
        db.session.rollback()
        return {"errors": [str(e)]}, 400

    except Exception as e:
        db.session.rollback()
        return {"errors": ["An internal server error occurred"]}, 500