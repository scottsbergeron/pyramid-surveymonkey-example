from pyramid.view import view_defaults


@view_defaults(route_name='request_example', renderer='templates/examples/request.jinja2')
class RequestExampleView:

    def __init__(self, request):
        self._request = request

    def get(self):
        return {
            'path_params': self._request.matchdict,
            'query_params': self._request.params
        }


def includeme(config):
    # This route will only be matched if variable1 and variable2 are supplied. variable1 must be an integer.
    config.add_route('request_example', '/example/request/{variable1:\d+}/{variable2}')
    config.add_view(RequestExampleView, attr='get', request_method='GET')
