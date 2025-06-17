import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from server.app import app
from server.models import db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

with app.app_context():
    db.drop_all()
    db.create_all()

    r1 = Restaurant(name="Domino's", address="123 Street")
    r2 = Restaurant(name="Kiki's Pizza", address="456 Avenue")

    p1 = Pizza(name="Emma", ingredients="Dough, Tomato Sauce, Cheese")
    p2 = Pizza(name="BBQ Chicken", ingredients="Dough, BBQ Sauce, Chicken, Cheese")

    db.session.add_all([r1, r2, p1, p2])
    db.session.commit()

    rp1 = RestaurantPizza(price=10, pizza_id=p1.id, restaurant_id=r2.id)
    rp2 = RestaurantPizza(price=15, pizza_id=p2.id, restaurant_id=r1.id)

    db.session.add_all([rp1, rp2])
    db.session.commit()
