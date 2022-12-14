"""Clean Code in Python - Chapter 3: General traits of good code

> Keep It Simple
"""


class ComplicatedNamespace:
    """An convoluted example of initializing an object with some properties.
    Instead of using a simple constructor, it uses a class method to validate the keys of **kwargs

    >>> cn = ComplicatedNamespace.init_with_data(
    ...    id_=42, user="root", location="127.0.0.1", extra="excluded"
    ... )
    >>> cn.id_, cn.user, cn.location
    (42, 'root', '127.0.0.1')

    >>> hasattr(cn, "extra")
    False

    """

    ACCEPTED_VALUES = ("id_", "user", "location")

    @classmethod
    def init_with_data(cls, **data):
        instance = cls()
        for key, value in data.items():
            if key in cls.ACCEPTED_VALUES:
                setattr(instance, key, value)
        return instance


class Namespace:
    """Create an object from keyword arguments.

    >>> cn = Namespace(
    ...    id_=42, user="root", location="127.0.0.1", extra="excluded"
    ... )
    >>> cn.id_, cn.user, cn.location
    (42, 'root', '127.0.0.1')

    >>> hasattr(cn, "extra")
    False
    """

    ACCEPTED_VALUES = ("id_", "user", "location")

    def __init__(self, **data):
        for attr_name, attr_value in data.items():
            if attr_name in self.ACCEPTED_VALUES:
                setattr(self, attr_name, attr_value)
