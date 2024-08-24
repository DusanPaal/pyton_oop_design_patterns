from abc import ABCMeta, abstractmethod
from unittest import TestCase, TextTestRunner

# Description:
# ------------
# The module provides an implementation of the factory pattern
# to create related or dependent objects. The Factory design
# pattern adds an extra level of abstraction to creating specific objects
# while hiding the instantioation details from the class or method
# that is using it. Thus, the factory pattern represents an interface
# that defers the creation of the final object to a subclass.

# Useful when:
# ------------
# - there is need to provide a library of relatively
#   similar products from a single factory.
# - the system needs to be independent of how the products
#   are created.
# - intention to enforce consistent interfaces across products.
# - You want to localize knowledge of the specifics of instantiating a particular object to the
# subclass so that the client doesn't need to be concerned about the details.
#
# Key features:
# ------------
# - defers the creation of the final object to a subclass
# - inserts another layer/abstraction between instantiating an object
#   and where in the code it is actually used.
# - It is unknown what or how many objects will need to be created until runtime.


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
