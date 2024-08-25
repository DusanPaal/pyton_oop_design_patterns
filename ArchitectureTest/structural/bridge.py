"""
Description.
------------
The Bridge Pattern is designed to decouple an abstraction from its implementation,
allowing you to change or extend both independently without affecting each other.
This pattern is particularly useful when a system's code is tightly coupled with
its logic and abstraction, restricting the ability to extend or modify either
side without significant changes.

Key features:
-------------
Decoupling:
    The Bridge Pattern separates the abstraction (the high-level interface)
    from the implementation (the low-level operations), allowing both to be
    developed and modified independently.

Composition Over Inheritance:
    Unlike the Adapter Pattern, which is more about creating a new interface
    on top of existing code, the Bridge Pattern uses composition to establish
    a dynamic relationship between the abstraction and the implementation.
    This is done at runtime rather than being hard-coded in the class definitions.

Refactoring Existing Code:
    The Bridge Pattern is often applied to refactor existing codebases where
    abstraction and implementation are tightly integrated. It creates a more
    flexible design that allows both sides to be extended or modified independently.

Comparison with Other Patterns:
-------------------------------
Adapter Pattern:
    While both patterns involve interfaces and aim to bridge gaps, the Adapter
    focuses on adapting an existing interface to meet new requirements, often
    without changing existing code. In contrast, the Bridge Pattern is used to
    separate abstraction from implementation and is more about refactoring
    existing code to make it more flexible.

Decorator Pattern:
    The Decorator adds responsibilities to an object without altering its interface,
    whereas the Bridge Pattern separates the abstraction from its implementation,
    focusing on decoupling and independent extensibility.

Facade Pattern:
    The Facade Pattern provides a simplified interface to a complex subsystem,
    whereas the Bridge Pattern aims at decoupling abstraction and implementation
    to allow them to evolve separately.

Usage:
------
Tight Coupling Issues:
    When your system's abstraction and implementation are tightly
    coupled, making it difficult to extend or modify one without
    affecting the other. The Bridge Pattern helps separate these concerns.

Extending Abstraction and Implementation Independently:
    When you want to break down a solution into smaller, independent
    conceptual parts, allowing each to evolve or be extended separately
    without impacting the other.
"""

from abc import ABCMeta, abstractmethod
from unittest import TestCase, TextTestRunner


# ==========================================
#           abstraction classes
# ==========================================
class IAbstraction(metaclass=ABCMeta):
    """The abstraction interface"""

    @staticmethod
    @abstractmethod
    def method(*args):
        """The method handle"""

class RefinedAbstractionA(IAbstraction):
    """The refined abstraction class A"""

    def __init__(self, implementer):
        self.implementer = implementer()

    def method(self, *args):
        return self.implementer.method(*args)

class RefinedAbstractionB(IAbstraction):
    """The refined abstraction class B"""

    def __init__(self, implementer):
        self.implementer = implementer()

    def method(self, *args):
        return self.implementer.method(*args)


# ==========================================
#           implementer classes
# ==========================================
class IImplementer(metaclass=ABCMeta):
    """The implementer interface"""

    @staticmethod
    @abstractmethod
    def method(*args: tuple) -> list:
        """The method implementation"""

class ConcreteImplementerA(IImplementer):
    """The concrete implementer class A"""

    @staticmethod
    def method(*args: tuple) -> list:
        return list(args)

class ConcreteImplementerB(IImplementer):
    """The concrete implementer class A"""

    @staticmethod
    def method(*args: tuple) -> list:
        return [arg + 1 for arg in args]


# ==========================================
#                   tests
# ==========================================
if __name__ == "__main__":

    class TestBridgePattern(TestCase):
        """A Test Class for the Bridge Pattern"""

        def test_bridge_pattern(self):
            """A test method to test the bridge pattern"""

            ref_abstr_a = RefinedAbstractionA(ConcreteImplementerA)
            self.assertEqual(ref_abstr_a.method(1, 2, 3), [1, 2, 3])

            ref_abstr_b = RefinedAbstractionB(ConcreteImplementerB)
            self.assertEqual(ref_abstr_b.method(1, 2, 3), [2, 3, 4])

    runner = TextTestRunner()
    runner.run(TestBridgePattern('test_bridge_pattern'))