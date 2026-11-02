from flask import Flask
from .health import health_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(health_bp)
    return app