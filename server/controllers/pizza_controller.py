from server import db
from server.models import Pizza # Only need Pizza model for this route

def get_pizzas():
    pizzas = Pizza.query.all()
    return [p.to_dict() for p in pizzas]

# Future functions for other pizza routes would go here if required (not required by prompt)