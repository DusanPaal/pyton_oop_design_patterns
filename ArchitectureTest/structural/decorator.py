"""
Description:
------------
The Decorator Pattern is a structural design pattern that enables adding
new functionalities to an object dynamically at runtime. This pattern is
especially useful when you need to extend an object's behavior without
altering its original structure or class.

Key features:
------------
Applicability in Both Paradigms:
    The Decorator Pattern can be used in both Object-Oriented Programming
    and Functional Programming.

Different from Python Language Decorators:
    While the concept of "wrapping" is shared, the structural pattern is
    distinct from Python's syntactic decorators, as it allows runtime manipulation.

Extensibility Without Modification:
    Decorators forward requests to the original object and can perform
    additional actions, providing extensibility without altering the original object.

Nesting and Recursion:
    Decorators can be nested recursively, enabling complex behavior combinations
    without subclassing.

Flexibility Over Inheritance:
    Compared to static inheritance, decorators offer more flexibility by allowing
    you to dynamically add or remove behaviors at runtime.

Supports Recursive Composition:
    The pattern can be used recursively, applying the same decorator multiple
    times in a chain (e.g., halve(halve(number))).

Non-Invasive:
    A well-implemented decorator does not modify the internal state or references
    of the original object, ensuring the base object remains unchanged if the decorator
    is removed.

Usage:
------
Dynamic Functionality Extension:
    You want to extend an object's functionality at runtime without modifying
    its class.

Reversible Changes:
    You need the ability to remove or alter the added functionality later on,
    reverting to the object's original state.

Avoiding Subclass Explosion:
    Instead of creating multiple subclasses to cover all possible combinations
    of functionalities, decorators allow you to mix and match behaviors dynamically.
"""

from abc import ABCMeta, abstractmethod
from unittest import TestCase, TextTestRunner

class IComponent(metaclass=ABCMeta):
    """The Interface for the Component"""

    @staticmethod
    @abstractmethod
    def decorated_method(self):
        """A method to implement"""

class ConcreteComponent(IComponent):
    """A component that can be decorated or not"""

    def decorated_method(self):
        """Method intrinsic to the component"""
        return "Component Intrinsic Method"

class Decorator(IComponent):
    "The Decorator also implements the IComponent"

    def __init__(self, obj):
        "Set a reference to the decorated object"
        self.object = obj

    def decorated_method(self):
        "A decorating method"
        return f"Decorator method({self.object.decorated_method()})"


# ==========================================
#                   tests
# ==========================================
if __name__ == "__main__":

    class TestDecoratorPattern(TestCase):
        """A Test Class for the Decorator Pattern"""

        def test_decorator_pattern(self):
            """A test method to test the decorator pattern"""

            component = ConcreteComponent()
            self.assertEqual(
                component.decorated_method(),
                "Component Intrinsic Method"
            )

            decorator = Decorator(component)
            self.assertEqual(
                decorator.decorated_method(),
                "Decorator method(Component Intrinsic Method)"
            )

    runner = TextTestRunner()
    runner.run(TestDecoratorPattern('test_decorator_pattern'))