# Description.
# ------------
# The Bridge pattern is a structural pattern that decouples an abstraction from its
# implementation so that the two can vary independently.
#
# Useful when:
# ------------
# - the code of a system is tightly coupled with the logic and abstraction too close together,
#   that is limiting the choices in how the solution can be extended in the required direction.
# - Use when you want to separate a solution where the abstraction and implementation may be
#   tightly coupled and you want to break it up into smaller conceptual parts; Once you have
#   added the bridge abstraction, you should be able to extend each side of it
#   separately without breaking the other
#
# Key features:
# ------------
# - decouples the abstraction from the implementation
# - similar to the Adapter pattern except in the intent that you developed it.
# - The Bridge is an approach to refactor already existing code, whereas the Adapter creates an
#   interface on top of existing code through existing available means without refactoring any
#   existing code or interfaces.
# - the application of a Bridge in your code should use composition instead of inheritance,
#   the relationship is assigned at runtime, rather than hard coded in the class definition

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