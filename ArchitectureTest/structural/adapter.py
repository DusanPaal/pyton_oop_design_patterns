"""
Description:
------------
The Adapter Pattern is used to make an interface compatible
with another interface that a client expects. It involves
creating an adapter class that translates the interface of
a class into an interface that the client can work with.
This pattern allows for the integration of existing code
with new code without altering the existing codebase.

Key Features:
-------------
Incompatible Interfaces:
    When you have an existing class or interface that does
    not match the interface required by the client or system.
   The Adapter Pattern allows you to create a new interface
   that is compatible with the client’s expectations.

Legacy Code Integration:
    When integrating with legacy systems or third-party libraries
   where modifying the original interface is not possible or practical.

Providing Additional Functionality:
    When you want to adapt an existing interface to meet new requirements,
    potentially adding additional functionality in the process.

Distinction from Other Patterns:
--------------------------------
Facade:
    While both patterns provide a simpler interface, the Adapter Pattern
    specifically focuses on making incompatible interfaces work together,
    whereas the Facade Pattern provides a unified interface over a set of
    interfaces.

Decorator:
    The Adapter changes the interface of an object to match the client's
    expectations, whereas the Decorator adds additional behavior to an object
    without modifying its interface.

Bridge:
    The Adapter Pattern adapts existing interfaces to meet new requirements,
    while the Bridge Pattern is used to decouple an abstraction from its
    implementation, making it easier to vary or extend both independently.

Usage:
------
Alternative Interface:
    The Adapter Pattern provides an alternative interface to an existing
    interface, allowing it to work with code that expects a different interface.
    This can involve modifying method signatures, combining methods, or transforming
    data.

Wrapper Concept:
    Similar to the Decorator Pattern, the Adapter Pattern wraps an object to
    provide a new interface. However, unlike the Decorator, which adds
    responsibilities or features without changing the existing interface,
    the Adapter changes the interface to make it compatible.

Runtime Adaptation:
    Adapters are used at runtime to adapt objects to the expected interface,
    but they are not designed for recursive use.
"""

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