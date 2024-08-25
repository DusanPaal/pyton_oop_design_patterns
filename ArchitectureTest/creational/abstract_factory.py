"""
Description:
------------
The Abstract Factory Pattern provides an interface for creating families
of related or dependent objects without specifying their concrete classes.
It's a higher-level design pattern that adds an abstraction layer over other
creational patterns like the Factory Method Pattern.

Key features:
-------------
Same Use Cases as Factory Method:
    The Abstract Factory Pattern can be used in similar scenarios as
    the Factory Method, but it provides a factory for creational pattern
    methods rather than directly creating products.

Client-Side Abstraction:
   The client interacts with the abstract factory interface rather than
   handling internal logic and factory implementations, allowing easier
   integration and extension.

Defers Final Product Creation:
    The actual creation of products is deferred to concrete
    factory subclasses that implement the abstract factory.

Usage:
------
Multiple Similar Products:
    When you need to provide a library of similar
    products that come from different factories.

Decoupling Product Creation
    When the system needs to be independent
    of how the products are created.

Consistent Interfaces:
    When you want to enforce consistent
    interfaces across different products.

Exchanging Product Families:
    When there is a need to switch
    between different families of products.
"""

from abc import ABCMeta, abstractmethod
from unittest import TestCase, TextTestRunner, TestSuite

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
#         concrete factory classes
# ==========================================
class FactoryA:
    """The A-factory Class"""

    @staticmethod
    def create_object(product_property):
        """A static method that creates a product"""

        # create a concrete product class
        # based on a specific product property
        try:
            if product_property == "a":
                return ConcreteProductA()
            if product_property == "b":
                return ConcreteProductB()
            if product_property == "c":
                return ConcreteProductC()
        except NameError as exc:
            print(exc)

        # ideally, the code should never reach here
        # but if it does, the method should return None
        return None

class FactoryB:
    """The B-factory Class"""

    @staticmethod
    def create_object(product_property):
        """A static method that creates a product"""

        # create a concrete product class
        # based on a specific product property
        try:
            if product_property == "a":
                return ConcreteProductA()
            if product_property == "b":
                return ConcreteProductB()
            if product_property == "c":
                return ConcreteProductC()
        except NameError as exc:
            print(exc)

        # ideally, the code should never reach here
        # but if it does, the method should return None
        return None

class FactoryC:
    """The C-factory Class"""

    @staticmethod
    def create_object(product_property):
        """A static method that creates a product"""

        # create a concrete product class
        # based on a specific product property
        try:
            if product_property == "a":
                return ConcreteProductA()
            if product_property == "b":
                return ConcreteProductB()
            if product_property == "c":
                return ConcreteProductC()
        except NameError as exc:
            print(exc)

        # ideally, the code should never reach here
        # but if it does, the method should return None
        return None


# ==========================================
#         abstract factory classes
# ==========================================
class IAbstractFactory(metaclass=ABCMeta):
    """Abstract Factory Interface"""

    @staticmethod
    @abstractmethod
    def create_object(factory):
        """The static Abstract factory interface method"""

class AbstractFactory(IAbstractFactory):
    """The Abstract Factory Concrete Class"""

    @staticmethod
    def create_object(factory):
        """Static get_factory method"""

        # create a concrete factory class
        # based on a specific factory property
        try:
            if factory in ['aa', 'ab', 'ac']:
                return FactoryA().create_object(factory[1])
            if factory in ['ba', 'bb', 'bc']:
                return FactoryB().create_object(factory[1])
            if factory in ['ca', 'cb', 'cc']:
                return FactoryC().create_object(factory[1])
        except Exception as exc:
            print(exc)

        # ideally, the code should never reach here
        # but if it does, the method should return None
        return None


# ==========================================
#                   tests
# ==========================================
if __name__ == "__main__":

    class TestAbstractFactoryPattern(TestCase):
        """A Test Class for the Factory Pattern"""

        def test_factory_a(self):
            """A method to test the factory A class"""

            product_a = AbstractFactory.create_object("aa")
            self.assertIsInstance(product_a, ConcreteProductA)

            product_b = AbstractFactory.create_object("ab")
            self.assertIsInstance(product_b, ConcreteProductB)

            product_c = AbstractFactory.create_object("ac")
            self.assertIsInstance(product_c, ConcreteProductC)

        def test_factory_b(self):
            """A method to test the factory A class"""

            product_a = AbstractFactory.create_object("ba")
            self.assertIsInstance(product_a, ConcreteProductA)

            product_b = AbstractFactory.create_object("bb")
            self.assertIsInstance(product_b, ConcreteProductB)

            product_c = AbstractFactory.create_object("bc")
            self.assertIsInstance(product_c, ConcreteProductC)

        def test_factory_c(self):
            """A method to test the factory A class"""

            product_a = AbstractFactory.create_object("ca")
            self.assertIsInstance(product_a, ConcreteProductA)

            product_b = AbstractFactory.create_object("cb")
            self.assertIsInstance(product_b, ConcreteProductB)

            product_c = AbstractFactory.create_object("cc")
            self.assertIsInstance(product_c, ConcreteProductC)

    runner = TextTestRunner()
    runner.run(TestAbstractFactoryPattern('test_factory_a'))
    runner.run(TestAbstractFactoryPattern('test_factory_b'))
    runner.run(TestAbstractFactoryPattern('test_factory_c'))