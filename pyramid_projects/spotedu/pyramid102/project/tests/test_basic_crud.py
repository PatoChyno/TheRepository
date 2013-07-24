import transaction

from pyramid import testing

from ..models import DBSession

from ..models.user import User
from ..models.task import Task
from . import DatabaseTestCase
from ..views.views import (
        create_task,
        user_task,
        )
from mock import Mock
from pyramid.httpexceptions import (
    HTTPException,
    HTTPNotFound,
    HTTPFound,
    HTTPForbidden,
    )

class TestBasicCrud(DatabaseTestCase):

    def set_up(self):
        request = testing.DummyRequest()
        request.db_session = self.db_session
        request.route_url = Mock()
        u1=User('u1', 'u1@u.sk')
        u2=User('u2', 'u2@u.sk')
        t1=Task('t1', u1)
        t2=Task('t2', u2)
        u1.tasks=[t1]
        u2.tasks=[t2]
        self.u1=u1
        self.u2=u2
        self.t1=t1
        self.t2=t2
        request.db_session.add_all([u1,u2,t1,t2])
        request.db_session.commit()
        self.request=request

    def tear_down(self):
        pass

    def test_backlinks_working_properly(self):
        self.assertIn(self.t1.user, [self.u1, self.u2])
        self.assertIn(self.t2.user, [self.u1, self.u2])

    def test_everything_created(self):
        tasks=self.request.db_session.query(Task).all()
        self.assertEqual(len(tasks),2)
        users=self.request.db_session.query(User).all()
        self.assertEqual(len(users),2)
        self.assertEqual(len(users[0].tasks),1)
        self.assertEqual(len(users[1].tasks),1)


    def test_create_task(self):
        self.request.POST={'user_id':self.u1.id, 'task':'novy_task'}
        response=create_task(self.request)
        self.assertEqual(type(response), HTTPFound)
        self.assertEqual(len(self.u1.tasks), 2)
        self.assertEqual(len(self.u2.tasks), 1)
        self.assertIn('novy_task', [task.task for task in self.u1.tasks])


    def test_user_task(self):
        self.request.matchdict={'user_id':self.u1.id}
        response=user_task(self.request)
        self.assertEqual(response['user'], self.u1)
        self.assertEqual(response['tasks'], self.u1.tasks)
        



        
        
