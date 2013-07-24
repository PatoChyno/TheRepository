from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import (
    DBSession,
    Base,
    )

from pyramid.events import (
    ContextFound,
    )

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)


    #route configuration
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('pokus', '/pokus')
    config.add_route('tasks', '/tasks')
    config.add_route('create_task', '/create_task')
    config.add_route('user_task', '/user_task/{user_id}')
    config.add_route('list_all_users', '/list_all_users')


    def prepare_request(event): #{{{
        request = event.request
        request.settings = settings
        request.db_session = DBSession
    #}}}

    config.add_subscriber(prepare_request, ContextFound)

    config.scan()
    return config.make_wsgi_app()
