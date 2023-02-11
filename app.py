from flask import Flask

from utils.api_routes import ApiRoutes


def create_app():
    _app = Flask(__name__)
    _app.config.from_object('settings')
    _app = ApiRoutes.customer_apis(_app)
    return _app


app = create_app()

if __name__ == '__main__':
    app.run()
