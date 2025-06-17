
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask
from flask_migrate import Migrate
from server.config import Config
from server.models import db
from server.controllers.restaurant_controller import restaurant_bp
from server.controllers.pizza_controller import pizza_bp
from server.controllers.restaurant_pizza_controller import restaurant_pizza_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

# Blueprints
app.register_blueprint(restaurant_bp)
app.register_blueprint(pizza_bp)
app.register_blueprint(restaurant_pizza_bp)
