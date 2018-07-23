from pyramid.view import view_defaults

@view_defaults(route_name='home', renderer='string')
class HomeController:

    def __init__(self, request):
        self._request = request

    def get(self):
        return {'content':'hello'}

def includeme(config):
    config.add_route('home', '/home')
    config.add_view(HomeController, attr='get', request_method='GET')
