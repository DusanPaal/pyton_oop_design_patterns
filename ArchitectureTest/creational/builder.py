"""
Description:
------------
The Builder Pattern is a creational design pattern that aims
to separate the construction of a complex object from its
representation. This separation allows the same construction
process to create different representations of the object,
making it versatile and adaptable to different needs.

Key features:
-------------
Creational Pattern for Complex Objects:
    Unlike simpler creational patterns like the Factory Pattern,
    the Builder Pattern is specifically designed to handle the
    creation of more complex objects.

Flexible Construction:
    The Builder Pattern allows constructing complex objects in
    any order, including or excluding components as needed.
    This flexibility is crucial when dealing with objects that
    can be composed of many different parts.

Use of a Director:
    To handle different combinations of products or components,
    a specific Director can be used to create bespoke (custom).
    combinations. The Director controls the construction process,
    ensuring that the appropriate steps are followed.

Usage:
------
Complex Object Construction:
    When an object is too complex to be created with
    a single step and requires a step-by-step process.

Multiple Representations:
    When you need to create different representations
    of the same type of object using the same construction process.

"""

from abc import ABCMeta, abstractmethod
from unittest import TestCase, TextTestRunner, TestSuite

# ==========================================
#               product classes
# ==========================================
class Product:
    """The Product Class"""

    def __init__(self):
        self.parts = []

# ==========================================
#             builder classes
# ==========================================
class IBuilder(metaclass=ABCMeta):
    """"The Builder Interface"""

    @staticmethod
    @abstractmethod
    def build_part_a():
        """Build part A of a product"""

    @staticmethod
    @abstractmethod
    def build_part_a():
        """Build part B of a product"""

    @staticmethod
    @abstractmethod
    def build_part_a():
        """Build part C of a product"""

    @staticmethod
    @abstractmethod
    def get_result():
        """Return the final product"""

class Builder(IBuilder):
    """The Concrete Builder."""

    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.parts.append("Part A")

    def build_part_b(self):
        self.product.parts.append("Part B")

    def build_part_c(self):
        self.product.parts.append("Part C")

    def get_result(self):
        return self.product


# ==========================================
#             director classes
# ==========================================
class Director:
    """The Director Class"""

    @staticmethod
    def construct():
        """Constructs and returns the final product"""
        builder = Builder()
        builder.build_part_a()
        builder.build_part_b()
        builder.build_part_c()
        return builder.get_result()


# ==========================================
#                   tests
# ==========================================
if __name__ == "__main__":

    class TestAbstractFactoryPattern(TestCase):
        """A Test Class for the Builder Pattern"""

        def test_builder(self):
            """A method to test the builder class"""

            product = Director.construct()
            self.assertEqual(product.parts, ['Part A', 'Part B', 'Part C'])

    runner = TextTestRunner()
    runner.run(TestAbstractFactoryPattern('test_builder'))