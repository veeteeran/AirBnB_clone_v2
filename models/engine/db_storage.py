#!/usr/bin/python3

"""
Database Storage module
"""
from sqlalchemy import Column, Table
import os
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.city import City
from models.base_model import BaseModel
os.environ['HBNB_ENV'] = "dev"
os.environ['HBNB_MYSQL_USER'] = "hbnb_dev"
os.environ['HBNB_MYSQL_PWD'] = "hbnb_dev_pwd"
os.environ['HBNB_MYSQL_HOST'] = "localhost"
os.environ['HBNB_MYSQL_DB'] = "hbnb_dev_db"
os.environ['HBNB_TYPE_STORAGE'] = "db"


class DBStorage:
    """ DataBase Storage class """
    __engine = None
    __session = None

    def __init__(self):
        """ Time to make some shit """
        from sqlalchemy import create_engine
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                        os.getenv('HBNB_MYSQL_USER'),
                        os.getenv('HBNB_MYSQL_PWD'),
                        os.getenv('HBNB_MYSQL_HOST'),
                        os.getenv('HBNB_MYSQL_DB'), pool_pre_ping=True))
        if os.getenv('HBNB_ENV') == "test" and self.__engine is not None:
            from models.base_model import Base
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Doing all of something """
        types = {
                'BaseModel': BaseModel, 'User': User, 'Place': Place,
                'State': State, 'City': City, 'Amenity': Amenity,
                'Review': Review
            }
        if cls is not None:
            the_type = types.get(cls)
            result = self.__session.query(the_type).all()
        else:
            result = self.__session.query(State, City).all()
        return_dict = {}
        for item in result:
            key = item.__class__.__name__ + "." + item.id
            value = item
            return_dict.update({key: value})
        return return_dict

    def new(self, obj):
        """ Adds a new object to the database """
        if obj is not None:
            self.__session.add(obj)
        self.save()

    def save(self):
        """ Saves the new stuff or whatever idk I'm drunk """
        self.__session.commit()

    def delete(self, obj):
        """ Deletes the object from DB Cooper """
        if obj is not None:
            self.__session.delete(obj)
        self.save()

    def reload(self):
        from models.base_model import BaseModel, Base
        from models.city import City
        from models.state import State
        from sqlalchemy.orm import sessionmaker, scoped_session
        if self.__engine is not None:
            Base.metadata.create_all(self.__engine)
        sesh_thing = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sesh_thing)
        self.__session = Session()
