from sqlalchemy import (
    Column,
    Integer,
    Text,
    ForeignKey
    )

from . import Base
from .user import User

from sqlalchemy.orm import (
        relationship,
        backref
    )

class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(Text)
    user_id = Column(Integer, ForeignKey('user.id'), index=True)
    user=relationship('User', backref=backref("tasks", cascade="all, delete-orphan"))

    def __init__(self, task, user):
        self.task = task
        self.user = user

    def __repr__(self):
        return "Task(id=%s, task=%s)"%(str(self.id) , self.task)

