from pyramid.config import Configurator


with Configurator() as config:
    # Include controllers
    config.include('webapp.controllers.home')

    app = config.make_wsgi_app()
