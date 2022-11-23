#!/usr/bin/python3
"""
Defines a new engine of storage
Database mode, to be used with SQLAlchemy
"""
from os import getenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
import models
from models.state import State
from models.city import City
from models.base_model import Base


class DBStorage:
    """
    Create our database with SQLAlchemy
    Alchemy is our best friend!
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Starting the engine
        """
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, pwd, host, database),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Perform query on the current database session
        # Must return a dictionary with all objects according
        to class name passed in cls argument
        """
        obj_dict = {}
        if cls != '':
            all_objs = self.__session.query(models.classes[cls]).all()
            for obj in all_objs:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                obj_dict[key] = obj
            return obj_dict
        else:
            for key, val in models.classes.items():
                if key != "BaseModel":
                    all_objs = self.__session.query(val).all()
                    if len(all_objs) > 0:
                        for obj in all_objs:
                            key = "{}.{}".format(
                                obj.__class__.__name__, obj.id)
                            obj_dict[key] = obj
            return obj_dict

    def new(self, obj):
        """Adds the object to the current db session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to current db session"""
        self.__session.commit()

    def delete(self, obj):
        """ Delete obj of current db session """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Commit all changes in database after
        the changings
        """
        self.__session = Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """close session, proper ending"""
        self.__session.close()
