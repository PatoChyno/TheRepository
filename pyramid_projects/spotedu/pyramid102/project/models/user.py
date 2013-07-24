from sqlalchemy import (
    Column,
    Integer,
    Text,
    ForeignKey
    )


from . import Base



class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(Text)
    name = Column(Text)

    def __init__(self, name, email):
        self.name = name
        self.email=email


    def __repr__(self):
        return 'User(name=%s, email=%s)'%(self.name, self.email)
