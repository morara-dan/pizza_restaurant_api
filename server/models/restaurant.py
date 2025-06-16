from server import db


class Restaurant(db.Model):
    __tablename__ = 'restaurants'

  
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(50), unique=True, nullable=False) #
    address = db.Column(db.String(100), nullable=False) # Restaurant address, cannot be null
    
    restaurant_pizzas = db.relationship('RestaurantPizza', backref='restaurant', cascade="all, delete-orphan")

   
    def __repr__(self):
        return f'<Restaurant {self.id}: {self.name}>'

  
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
        }

    def to_dict_with_pizzas(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            # Iterate through related restaurant_pizzas and then get their pizza details
            "pizzas": [rp.pizza.to_dict() for rp in self.restaurant_pizzas]
        }