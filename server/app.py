from flask import Flask
:

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs)

    register_views(app)
    return app


def register_views(app):
    views = []

    for view in views:
        app.register_blueprint(view)


