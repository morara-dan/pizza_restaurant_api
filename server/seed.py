# server/seed.py

from server.app import app
from server import db
from server.models import Restaurant, Pizza, RestaurantPizza

print("Starting database seeding...")

with app.app_context():
    # --- Clean up existing data ---
    print("Deleting existing data...")
    db.session.query(RestaurantPizza).delete()
    db.session.query(Pizza).delete()
    db.session.query(Restaurant).delete()

    # --- IMPORTANT: Comment out or remove these lines ---
    # db.session.execute(db.text("DELETE FROM sqlite_sequence WHERE name='restaurants';"))
    # db.session.execute(db.text("DELETE FROM sqlite_sequence WHERE name='pizzas';"))
    # db.session.execute(db.text("DELETE FROM sqlite_sequence WHERE name='restaurant_pizzas';"))
    # ----------------------------------------------------
    db.session.commit()
    print("Existing data deleted.")

    # --- Create sample Restaurants ---
    print("Creating restaurants...")
    r1 = Restaurant(name="Krusty Krab Pizza", address="Bikini Bottom")
    r2 = Restaurant(name="Pizza Planet", address="Andy's Room")
    r3 = Restaurant(name="Loot Lake Pizzaria", address="Fortnite Island")
    r4 = Restaurant(name="Mario's Mushroom Kingdom Pizza", address="Peach's Castle")
    db.session.add_all([r1, r2, r3, r4])
    db.session.commit()
    print("Restaurants created and committed.")

    # --- Create sample Pizzas ---
    # ... (rest of pizza creation code) ...
    print("Creating pizzas...")
    p1 = Pizza(name="Cheese Lover's", ingredients="Mozzarella, Cheddar, Provolone")
    p2 = Pizza(name="Pepperoni Supreme", ingredients="Pepperoni, Cheese, Tomato Sauce")
    p3 = Pizza(name="Veggie Delight", ingredients="Bell Peppers, Onions, Mushrooms, Olives")
    p4 = Pizza(name="Meat Feast", ingredients="Sausage, Bacon, Ham, Pepperoni")
    p5 = Pizza(name="Hawaiian Dream", ingredients="Pineapple, Ham")
    db.session.add_all([p1, p2, p3, p4, p5])
    db.session.commit()
    print("Pizzas created and committed.")

    # --- Create sample RestaurantPizzas ---
    # ... (rest of restaurant pizza creation code) ...
    print("Creating restaurant-pizza relationships...")
    rp_data = [
        {"restaurant": r1, "pizza": p1, "price": 10},
        {"restaurant": r1, "pizza": p2, "price": 12},
        {"restaurant": r1, "pizza": p5, "price": 15},
        {"restaurant": r2, "pizza": p1, "price": 8},
        {"restaurant": r2, "pizza": p3, "price": 11},
        {"restaurant": r2, "pizza": p4, "price": 14},
        {"restaurant": r3, "pizza": p2, "price": 9},
        {"restaurant": r3, "pizza": p3, "price": 10},
        {"restaurant": r3, "pizza": p5, "price": 13},
        {"restaurant": r4, "pizza": p1, "price": 10},
        {"restaurant": r4, "pizza": p4, "price": 16},
        {"restaurant": r4, "pizza": p2, "price": 12},
    ]

    try:
        for item in rp_data:
            rp = RestaurantPizza(
                restaurant=item["restaurant"],
                pizza=item["pizza"],
                price=item["price"]
            )
            db.session.add(rp)
        db.session.commit()
        print("Restaurant-Pizza relationships created and committed.")
    except Exception as e:
        db.session.rollback()
        print(f"Error during seeding restaurant-pizza relationships: {e}")
        print("Database seeding rolled back due to an error.")
        raise


print("Database seeding complete!")