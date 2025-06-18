import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from server import create_app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

app = create_app()

def seed_data():
    with app.app_context():
        
        db.drop_all()
        db.create_all()

        
        restaurants = [
            Restaurant(name="Pizza Palace", address="123 Main St"),
            Restaurant(name="Mario's Pizzeria", address="456 Oak Ave"),
            Restaurant(name="Kiki's Pizza", address="789 Pine Rd")
        ]
        db.session.add_all(restaurants)

        pizzas = [
            Pizza(name="Margherita", ingredients="Tomato sauce, mozzarella, basil"),
            Pizza(name="Pepperoni", ingredients="Tomato sauce, mozzarella, pepperoni"),
            Pizza(name="Hawaiian", ingredients="Tomato sauce, mozzarella, ham, pineapple")
        ]
        db.session.add_all(pizzas)
        db.session.commit()

        
        restaurant_pizzas = [
            RestaurantPizza(price=10, restaurant_id=1, pizza_id=1),
            RestaurantPizza(price=12, restaurant_id=1, pizza_id=2),
            RestaurantPizza(price=15, restaurant_id=2, pizza_id=1),
            RestaurantPizza(price=8, restaurant_id=3, pizza_id=3)
        ]
        db.session.add_all(restaurant_pizzas)
        db.session.commit()

        print("Database seeded successfully!")

if __name__ == '__main__':
    seed_data()