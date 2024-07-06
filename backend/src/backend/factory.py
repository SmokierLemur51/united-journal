from dotenv import load_dotenv
from flask import Flask


load_dotenv()


def create_app(**config_overrides):
	app = Flask(__name__, static_url_path='/static')
	
	# env config
	app.config.from_pyfile("settings.py")
	
	# config obj
	from .config import Config
	app.config.from_object(Config)
	
	# config overrides
	app.config.update(config_overrides)
	
	# sqlalchemy
	from .models.models import db
	db.init_app(app)
	
	""" Blueprints """
	# You land at the crm 
	from .blueprints.crm.routes import crm
	app.register_blueprint(crm)
	from .blueprints.sales.views import sales
	app.register_blueprint(sales)
	from .blueprints.orders.views import orders
	app.register_blueprint(orders)
	from .blueprints.purchasing.views import purchasing
	app.register_blueprint(purchasing)
	

	# create database tables
	with app.app_context():
		# db.drop_all()
		db.create_all()
	
    # send that sucker to the moon	
	return app
