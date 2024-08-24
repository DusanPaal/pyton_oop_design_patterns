"""
Description:
------------
The Builder Pattern is a creational pattern whose intent is to separate
the construction of a complex object from its representation so that the
same construction process can be used to create different representations.

Useful when:
------------

Key features:
------------
- the Builder pattern is a creational pattern that is used
to create more complex objects created by a factory.
- The Builder pattern should be able to construct complex objects in
any order and include/exclude whichever available components it likes.
- for different combinations of products than can be returned from
a Builder, use a specific Director to create the bespoke combination.

from abc import ABCMeta, abstractmethod
from unittest import TestCase, TextTestRunner, TestSuite
"""

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