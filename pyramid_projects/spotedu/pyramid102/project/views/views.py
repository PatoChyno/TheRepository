from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from ..models.user import User
from ..models.task import Task

from pyramid.httpexceptions import (
    HTTPException,
    HTTPNotFound,
    HTTPFound,
    HTTPForbidden,
    )


@view_config(route_name='pokus', renderer='project:templates/pokus.mako')
def pokus_view(request):
    return {}

@view_config(route_name='tasks', renderer='project:templates/tasks.mako')
def tasks(request):
    print('tu')
    tasks=request.db_session.query(Task).all()
    return {'tasks': tasks}

@view_config(route_name='create_task', request_method="GET", renderer='project:templates/create.mako')
def create_task_show(request):
    return {}

@view_config(route_name='create_task', request_method="POST")
def create_task(request):
    """
    vytvori task pre daneho usera. 
    post['task'] - popis tasku
    post['user_id'] - id usera
    """
    post=request.POST
    user=request.db_session.query(User).filter_by(id=post['user_id']).first()
    task=Task(task=post['task'], user=user)
    request.db_session.add(task)
    return HTTPFound(request.route_path('tasks'))

@view_config(route_name='create_user', request_method="POST")
def create_user(request):
    """
    vytvori usera
    """
    post=request.POST
    task=request.db_session.query(Task).filter_by(id=post['id']).first()
    user=User(user=post['user'], task=task)
    request.db_session.add(user)
    return HTTPFound(request.route_path('tasks'))


@view_config(route_name='delete_task', request_method="POST")
def delete_task(request):
    """
    zmaze task pre daneho usera
    """
    post=request.POST
    task=request.db_session.query(Task).filter_by(id=post['id']).first()
    request.db_session.delete(task)
    return HTTPFound(request.route_path('tasks'))

@view_config(route_name='delete_user', request_method="POST")
def delete_user(request):
    """
    zmaze daneho usera
    """
    post=request.POST
    user=request.db_session.query(User).filter_by(id=post['user_id']).first()
    task=request.db_sesssion.query(Task).filter_by(id=post['id']).first()
    request.db_session.delete(user)
    request.db_session.delete(task)
    return HTTPFound(request.route_path('tasks'))

@view_config(route_name='list_all_users', request_method="GET" renderer='project:templates/list_all_users.mako')
def list_all_users(request):
    """
    vrati vsetkych userov
    """
    return request.db_session.query(User).filter_by(id=post['user_id']).all()

#TODO: dorobit create_user, delete_task, list_all_users, delete_user

    
@view_config(route_name='user_task', request_method="GET", renderer='project:templates/user_task.mako' )
def user_task(request):
    """
    zobrazi tasky pre daneho usera; matchdict obsahuje user_id.
    """
    dct=request.matchdict
    user=request.db_session.query(User).filter_by(id=dct['user_id']).first()
    return {'tasks': user.tasks, 'user': user}
