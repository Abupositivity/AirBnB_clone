self.id = str(uuid.uuid4())
self.created_at = datetime.now()
self.updated_at = datetime.now()
storage.new(self)

def __str__(self):
        """Returns a human-readable string representation
        of an instance"""

return "[{}] ({}) {}".\
format(type(self).__name__, self.id, self.__dict__)

def save(self):
        """Updates the updated_at attribute
        with the current datetime."""

self.updated_at = datetime.now()
storage.save()

def to_dict(self):
"""Returns a dictionary representation of an instance."""

my_dict = self.__dict__.copy()
my_dict["__class__"] = type(self).__name__
my_dict["created_at"] = my_dict["created_at"].isoformat()
my_dict["updated_at"] = my_dict["updated_at"].isoformat(\
							)
        return my_dict
