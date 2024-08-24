# DEscription:
# ------------
#
#
# Useful when:
# ------------
# - there is an existing interface that doesn't directly map to anoter interface that the client requires
# . So, then you create the Adapter that has a similar functional role, but with a
# new compatible interface
#
# Key features:
# ------------
# - It is an alternative interface over an existing interface. It can also provide extra functionality that the
# interface being adapted may not already provide.
# - The adapter is similar to the "Facade", but you are modifying the method signature, combining other
# methods and/or transforming data that is exchanged between the existing interface and the client.

# - similar to the Decorator in the way that it also acts like a wrapper to an object.
# It is also used at runtime; however, it is not designed to be used recursively.



# Use the Adapter when you want to use an existing class, but its interface does not match what
# you need.
# The adapter adapts to the interface of its parent class for those situations when it is not viable
# to modify the parent class to be domain-specific for your use case.
# Adapters will most likely provide an alternative interface over an existing object, class or
# interface, but it can also provide extra functionality that the object being adapted may not
# already provide.
# An adapter is similar to a Decorator except that it changes the interface to the object, whereas
# the decorator adds responsibility without changing the interface. This also allows the
# Decorator to be used recursively.
# An adapter is similar to the Bridge pattern and may look identical after the refactoring has been
# completed. However, the intent of creating the Adapter is different. The Bridge is a result of
# refactoring existing interfaces, whereas the Adapter is about adapting over existing interfaces
# that are not viable to modify due to many existing constraints. E.g., you don't have access to
# the original code or it may have dependencies that already use it and modifying it would affect
# those dependencies negatively.

from abc import ABCMeta, abstractmethod
from unittest import TestCase, TextTestRunner



# ==========================================
#      classes that must work together
# ==========================================
class IA(metaclass=ABCMeta):
    """An interface for an object"""

    @staticmethod
    @abstractmethod
    def method_a():
        "An abstract method A"

class ClassA(IA):
    """A Sample Class the implements IA"""

    def method_a(self):
        return "method_a()"

class IB(metaclass=ABCMeta):
    "An interface for an object"

    @staticmethod
    @abstractmethod
    def method_b():
        "An abstract method B"

class ClassB(IB):
    "A Sample Class the implements IB"

    def method_b(self):
        return "method_b()"



# ==========================================
#              adapter class
# ==========================================

class AdapterToClassB(IA):
    """ClassB does not have a method_a,
    so we can create an adapter"""

    # we need to create an adapter to ClassB

    def __init__(self):
        self.class_b = ClassB()

    def method_a(self):
        "calls the class b method_b instead"

        # some code to adapt the method comes here

        # call the method_b from class_b
        self.class_b.method_b()



# ==========================================
#                   tests
# ==========================================
if __name__ == "__main__":

    class TestAdapterPattern(TestCase):
        """A Test Class for the Adapter Pattern"""

        def test_adapter_pattern(self):
            """A test method to test the adapter pattern"""

            adapter = AdapterToClassB()
            self.assertEqual(
                adapter.method_a(),
                "method_b()"
            )

    runner = TextTestRunner()
    runner.run(TestAdapterPattern('test_adapter_pattern'))