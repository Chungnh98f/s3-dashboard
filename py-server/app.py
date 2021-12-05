from flask import Flask
from views.buckets import bucket_views
from views.files import file_views


def create_app(configs):
    app = Flask(__name__)
    app.config.from_object(configs)

    register_views(app)
    return app


def register_views(app):
    views = [
        bucket_views,
        file_views,
    ]

    for view in views:
        app.register_blueprint(view)
