"""
Description:
------------
The Factory Pattern is a creational design pattern that provides
an interface for creating objects, allowing subclasses to alter
the type of objects that will be created. This pattern adds an
extra level of abstraction by delegating the instantiation process
to subclasses, which means the client does not need to know the
specifics of how the objects are created.

Key features:
-------------
Deferred Object Creation:
    The creation of the final object is deferred to a subclass, meaning
    the specific class that creates the object is determined at runtime.

Added Abstraction Layer:
    By inserting another layer between the object instantiation and its usage
    in the code, the pattern allows for more flexible and maintainable code.

Runtime Flexibility:
    The Factory Pattern is useful when it is unknown what specific objects
    will need to be created until runtime, allowing the system to dynamically
    decide which class to instantiate.

Usage:
------
Library of Similar Products:
    When you need to create a group of similar products from a single factory.

Decoupling Object Creation:
    When the system needs to be independent of the object creation process,
    ensuring that the specifics of how objects are created are hidden from
    the client.

Consistent Interfaces:
    When there’s a need to enforce consistent interfaces across
    different products, ensuring they adhere to a particular standard.

Localized Knowledge of Instantiation:
    When you want to centralize the knowledge of how objects are instantiated
    within a subclass, so the client code is not concerned with these details.

"""

from abc import ABCMeta, abstractmethod
from unittest import TestCase, TextTestRunner

# ==========================================
#               product classes
# ==========================================
class IProduct(metaclass=ABCMeta):
    """A Hypothetical Class Interface (Product)"""

    @staticmethod
    @abstractmethod
    def create_object():
        """An abstract interface method"""

class ConcreteProductA(IProduct):
    """A Concrete Class that implements
    the IProduct interface"""

    def __init__(self):
        self.name = "ConcreteProductA"

    def create_object(self):
        return self

class ConcreteProductB(IProduct):
    """A Concrete Class that implements
    the IProduct interface"""

    def __init__(self):
        self.name = "ConcreteProductB"

    def create_object(self):
        return self

class ConcreteProductC(IProduct):
    """A Concrete Class that implements
    the IProduct interface"""

    def __init__(self):
        self.name = "ConcreteProductC"

    def create_object(self):
        return self


# ==========================================
#               factory class
# ==========================================
class Factory:
    """The Creator Class"""

    def create_object(self, product_property):
        """A static method that creates a product"""

        # create a concrete product class
        # based on a specific product property
        if product_property == "a":
            return ConcreteProductA()
        if product_property == "b":
            return ConcreteProductB()
        if product_property == "c":
            return ConcreteProductC()

        # ideally, the code should never reach here
        # but if it does, the method should return None
        return None


# ==========================================
#                   tests
# ==========================================
if __name__ == "__main__":

    class TestFactoryPattern(TestCase):
        """A Test Class for the Factory Pattern"""

        def test_factory_pattern(self):
            """A test method to test the factory pattern"""

            # check if the product is an instance of the ConcreteProductA class
            product_a = Factory().create_object("a")
            self.assertIsInstance(product_a, ConcreteProductA)

            # check if the product is an instance of the ConcreteProductB class
            product_b = Factory().create_object("b")
            self.assertIsInstance(product_b, ConcreteProductB)

            # check if the product is an instance of the ConcreteProductC class
            product_c = Factory().create_object("c")
            self.assertIsInstance(product_c, ConcreteProductC)

    runner = TextTestRunner()
    runner.run(TestFactoryPattern('test_factory_pattern'))
