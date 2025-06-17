
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))


from flask import Blueprint, jsonify
from server.models.pizza import Pizza

pizza_bp = Blueprint('pizzas', __name__)

@pizza_bp.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([{"id": p.id, "name": p.name, "ingredients": p.ingredients} for p in pizzas])
