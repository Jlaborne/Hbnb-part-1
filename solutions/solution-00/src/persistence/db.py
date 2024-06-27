"""
  Now is easy to implement the database repository. The DBRepository
  should implement the Repository (Storage) interface and the methods defined
  in the abstract class Storage.

  The methods to implement are:
    - get_all
    - get
    - save
    - update
    - delete
    - reload (which can be empty)
"""

from src.models.base import Base, db
from src.persistence.repository import Repository
from src.models.amenity import Amenity, PlaceAmenity
from src.models.city import City
from src.models.country import Country
from src.models.place import Place
from src.models.review import Review
from src.models.user import User
from utils.populate import populate_db

class DBRepository(Repository):
    """Dummy DB repository"""

    def __init__(self) -> None:
        """Not implemented"""

    def get_all(self, model_name: str) -> list:
        """Not implemented"""
        model_class = self._get_model_class(model_name)
        return model_class.query.all()

    def get(self, model_name: str, obj_id: str) -> Base | None:
        """Not implemented"""
        model_class = self._get_model_class(model_name)
        return model_class.query.get(obj_id)

    def reload(self) -> None:
        """Not implemented"""
        populate_db(self)

    def save(self, obj: Base) -> None:
        """Not implemented"""
        db.session.add(obj)
        db.session.commit()

    def update(self, obj: Base) -> Base | None:
        """Not implemented"""
        db.session.merge(obj)
        db.session.commit()
        return obj

    def delete(self, obj: Base) -> bool:
        """Not implemented"""
        db.session.delete(obj)
        db.session.commit()
        return True

    def _get_model_class(self, model_name: str) -> type[Base]:
        """Helper method to get model class by name"""
        models = {
            "amenity": Amenity,
            "city": City,
            "country": Country,
            "place": Place,
            "placeamenity": PlaceAmenity,
            "review": Review,
            "user": User,
        }
        return models[model_name]