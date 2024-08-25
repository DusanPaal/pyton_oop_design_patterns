"""
Description:
------------
The Prototype Pattern is a creational design pattern that is used
to create new objects by copying existing objects, rather than
creating new instances through traditional instantiation.
This pattern is particularly useful when object creation is
resource-intensive or when objects need to be dynamically created
at runtime without knowing their exact configurations in advance.

Key features:
-------------
Clone Method:
    The pattern typically involves a clone() method that is implemented by classes
    using the Prototype pattern. This method is responsible for copying the object,
    and it can be a shallow or deep copy depending on the implementation.

Runtime Object Creation:
    Just like other creational patterns, the Prototype Pattern facilitates
    the creation of objects at runtime. However, it does so by using an already
    instantiated object as a template.

Avoids Class Proliferation:
    The Prototype Pattern reduces the need for a large number of classes.
    Instead of creating new classes for every possible object configuration,
    you can create a prototype object and clone it as needed.

Flexible Cloning:
    When designing the clone() method, careful consideration is needed for
    how deep the copying should be. You can choose between shallow copying,
    deep copying, or a combination depending on the object's attributes and
    the desired behavior.

Usage:
------
Resource-Intensive Object Creation:
    When creating a new object is resource-intensive
    (e.g., requires significant computational resources or time),
    and it is more efficient to copy an existing object.

Dynamic Object Creation:
    When objects need to be created dynamically at runtime without
   knowing their exact attributes beforehand.

Reusing Configurations:
    When you have an object with a specific configuration
    that you want to reuse multiple times without recreating it from scratch.

"""

from abc import ABCMeta, abstractmethod
from unittest import TestCase, TextTestRunner, TestSuite
import copy


# ==========================================
#            prototype classes
# ==========================================
class IPrototype(metaclass=ABCMeta):
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
