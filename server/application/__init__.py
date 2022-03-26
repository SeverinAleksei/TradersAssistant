from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_redis import FlaskRedis
from flask_sqlalchemy import SQLAlchemy

# Globally accessible libraries
db = SQLAlchemy()
r = FlaskRedis()
jwt = JWTManager()
def create_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)

    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auth/db.sqlite'

    db.init_app(app)
    jwt.init_app(app)
    cors = CORS(app)

    with app.app_context():
        # Import parts of our application
        from .auth import auths
        from .forecast import forecast
        from .forecast import forecastprocessing
        # Register Blueprints
        app.register_blueprint(auths.auth_bp)
        app.register_blueprint(forecast.forecast_bp)
        app.register_blueprint(forecastprocessing.forecastprocessing_bp)
        return app
