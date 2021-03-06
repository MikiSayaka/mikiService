from pyramid.config import Configurator
from pyramid.events import subscriber, NewResponse


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)

    config.add_route('home', '/')
    config.add_route('listPostData', '/listPostData')
    config.add_route('listGetData', '/listGetData')

    config.scan()
    return config.make_wsgi_app()

@subscriber(NewResponse)
def add_access_list(event):
    event.response.headerlist.append(('Access-Control-Allow-Origin', '*'));
