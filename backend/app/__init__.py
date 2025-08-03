# from flask import Flask
# from .extensions import db, jwt, migrate, cors

# def create_app():
#     app = Flask(__name__)
#     app.config.from_object('app.config.Config')

#     # Initialize extensions
#     db.init_app(app)
#     jwt.init_app(app)
#     migrate.init_app(app, db)
#     cors.init_app(app)

#     # Register blueprints
#     from .routes.auth import auth_bp
#     from .routes.dashboard import dashboard_bp
#     app.register_blueprint(auth_bp)
#     app.register_blueprint(dashboard_bp)

#     return app

# app/__init__.py

from flask import Flask
from .extensions import db, jwt, migrate, cors

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    # Init extensions
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)

    # Register routes
    from .routes.auth import auth_bp
    from .routes.dashboard import dashboard_bp
    app.register_blueprint(auth_bp)       # now /login works
    app.register_blueprint(dashboard_bp)

    return app
