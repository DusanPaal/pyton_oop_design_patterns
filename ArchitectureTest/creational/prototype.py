# Description:
# ------------
# The Prototype design pattern is suitable for situations when
# creating new objects requires more resources than available.
# The resources can be saved by just creating a copy (deep or shallow)
# of any existing object that is already in memory. In the Prototype
# pattern interface, a static clone() method is created that should
# be implemented by all classes that use the interface.

# Useful when:
# ------------
# A prototype is also useful for when you want to create a copy of
# an object, but creating that copy may be very resource intensive.
#
# Key features:
# ------------




# Just like the other creational patterns, a Prototype is used to create an object at runtime.
# A Prototype is created from an object that is already instantiated. Imagine using the existing
# object as the class template to create a new object, rather than calling a specific class.
# The ability to create a Prototype means that you don't need to create many classes for specific
# combinations of objects. You can create one object, that has a specific configuration, and then
# clone this version many times, rather than creating a new object from a predefined class
# definition.
# New Prototypes can be created at runtime, without knowing what kind of attributes the
# prototype may eventually have. E.g., You have a sophisticated object that was randomly
# created from many factors, and you want to clone it rather than re applying all the same
# functions over and over again until the new object matches the original.
# - when designing your clone() method, you should consider which elements will be
# shallow copied, how deep, and whether or not full recursive deep copy is necessary.

from abc import ABCMeta, abstractmethod
from unittest import TestCase, TextTestRunner, TestSuite
import copy


# ==========================================
#            prototype classes
# ==========================================
class IPrototype:
    """The Prototype interface"""

    @staticmethod
    @abstractmethod
    def clone(mode="shallow"):
        """The clone, deep or shallow.
        It is up to you how you want to implement
        the details in your concrete class"""


class ConcretePrototype(IPrototype):
    """A concrete class that implements
    the IPrototype interface"""

    def __init__(self, field):
        self.field = field

    def clone(self, mode="shallow"):
        """This clone method uses
        a shallow copy technique"""

        if mode == "shallow":
            # results in a 1 level shallow copy of the Document
            fld = self.field
        if mode == "referential":
            # results in a 2 level shallow copy of the Document
            # since it also create new references for the 1st level
            # list elements as well
            fld = self.field.copy()
        if mode == "deep":
            # recursive deep copy. Slower but results in a new copy
            # where no sub elements are shared by reference
            fld = copy.deepcopy(self.field)

        return type(self)(fld)

    def __str__(self):
        return f"{id(self)}\tfield={self.field}\ttype={type(self.field)}"


# ==========================================
#                   tests
# ==========================================
if __name__ == "__main__":

    class TestPrototypePattern(TestCase):
        """A Test Class for the Prototype pattern"""

        def test_prototype_pattern(self):
            """A test method to test the prototype pattern"""

            proto_a = ConcretePrototype([1, 2, 3, 4])
            proto_b = proto_a.clone()
            self.assertEqual(proto_a.field, proto_b.field)
            self.assertNotEqual(f"{proto_a}", f"{proto_b}")

            proto_b.field[1] = 5;
            self.assertEqual(proto_a.field, proto_b.field)
            self.assertEqual(proto_a.field, [1, 5, 3, 4])

    runner = TextTestRunner()
    runner.run(TestPrototypePattern('test_prototype_pattern'))
