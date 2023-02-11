from utils.lazy_viewer import LazyView


class ApiRoutes:

    @staticmethod
    def customer_apis(app):
        app.add_url_rule("/api/v1/customer/<int:customer_id>", methods=['GET'],
                          view_func=LazyView('api.v1.get_customer'))

        app.add_url_rule("/api/v1/customer", methods=['POST'],
                          view_func=LazyView('api.v1.create_customer'))

        app.add_url_rule("/api/v1/customer/<int:customer_id>", methods=['PUT'],
                          view_func=LazyView('api.v1.update_customer'))

        app.add_url_rule("/api/v1/customer/<int:customer_id>", methods=['DELETE'],
                          view_func=LazyView('api.v1.delete_customer'))
        return app