from flask import Flask
from .health import health_bp
from .projects import projects_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(health_bp)
    app.register_blueprint(projects_bp)
    return app