from server import db 
from sqlalchemy.ext.associationproxy import association_proxy 
from sqlalchemy.orm import validates 

class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizzas'

   
    id = db.Column(db.Integer, primary_key=True) 
    price = db.Column(db.Integer, nullable=False) 

    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)

    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'), nullable=False)


    def __repr__(self):
        return f'<RestaurantPizza {self.id} (R_id:{self.restaurant_id}, P_id:{self.pizza_id}) Price:{self.price}>'


    @validates('price')
    def validate_price(self, key, price):

        if not (1 <= price <= 30):
            raise ValueError("Price must be between 1 and 30")
        return price


    def to_dict(self):
        return {
            "id": self.id,
            "price": self.price,
            "pizza_id": self.pizza_id,
            "restaurant_id": self.restaurant_id,
        }


    def to_dict_full(self):
        return {
            "id": self.id,
            "price": self.price,
            "pizza_id": self.pizza_id,
            "restaurant_id": self.restaurant_id,

            "pizza": self.pizza.to_dict(),      
            "restaurant": self.restaurant.to_dict()
        }