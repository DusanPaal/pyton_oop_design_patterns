# Description:
# ------------
# The decorator pattern is a structural pattern, that allows
# to attach additional responsibilities to an object at runtime.
#
# Useful when:
# ------------
# - the functionality of a object needs to be extended dynamically
#   with new responsibilities without altering the class
# - the new responsibility must be later removed from the decorated
#   object when it's no longer needed.
#
# Key features:
# ------------
# - can be used in both the Object Oriented and Functional paradigms.
# - is different than the Python language feature of Python Decorators in its
#   syntax and complete purpose. It is a similar concept in the way that it is
#   a wrapper, but it also can be applied at runtime dynamically.
# - adds extensibility without modifying the original object by forwarding
#   requests to the enclosed object and can perform extra actions.
# - decorators can be nested recursively.
# - It is an alternative method to creating multiple combinations of subclasses,
#   e.g. instead of creating a subclass with all combinations of objects A, B, C
#   in any order, and including/excluding objects, 3 objects can be created that
#   can decorate each other in any order, e.g., (D(A(C))) or (B(C)) or (A(B(A(C))).
# - The decorator, compared to using static inheritance to extend, is more flexible
#   since it can be easily add/remove the decorators at runtime. E.g., use in a
#   recursive function
# - supports recursive composition. E.g., halve(halve(number))
# - A decorator shouldn't modify the internal objects data or references.
#   This allows the original object to stay intact if the decorator is later removed

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