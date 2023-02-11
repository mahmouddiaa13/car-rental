from werkzeug.utils import import_string, cached_property


class LazyView(object):

    def __init__(self, import_name):
        self.middle_wares = []
        self.__module__, self.__name__ = import_name.rsplit('.', 1)
        self.import_name = import_name

    @property
    def view_with_middleware(self):
        view = self.view
        for middle_ware in reversed(self.middle_wares):
            view = middle_ware(view)
        return view

    @cached_property
    def view(self):
        return import_string(self.import_name)

    def __call__(self, *args, **kwargs):
        response = self.view_with_middleware(*args, **kwargs)
        return response
