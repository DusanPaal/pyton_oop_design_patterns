# Description:
# ------------
# The module provides an implementation of the "abstract factory pattern"
# using the "factory pattern" to create a family of related or dependent
# objects. The Abstract Factory Pattern adds an abstraction layer over
# multiple other creational pattern implementations.

# Useful when:
# ------------
# - there is need to provide a library of relatively
#   similar products from multiple different factories.
# - the system needs to be independent of how the products
#   are created.
# - intention to enforce consistent interfaces across products.
# - there is the possibility to exchange product families.
#
# Key features:
# ------------
# - fulfills all of the same use cases as the Factory method,
#   but is a factory for creational pattern type methods.
# - The client implements the abstract factory interface,
#   rather than all the internal logic and Factories. This
#   allows the possibility of creating a library that can be
#   imported for using the Abstract Factory.
# - The Abstract Factory defers the creation of the final
#   products/objects to its concrete factory subclasses.

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