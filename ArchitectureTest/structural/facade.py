"""
Description:
------------
The Facade Pattern is a structural design pattern that provides a simplified,
unified interface to a complex system consisting of multiple subsystems.
This pattern creates a higher-level interface that makes the system easier
to use and understand.

Key features:
-------------
Simplified Interface:
    The Facade pattern provides a simple and easy-to-use interface
    that masks the underlying complexity of the system.

Hides Complexity:
    It hides the intricate workings of the subsystems from the client,
   making interactions with the system more straightforward.

Decoupling:
    The pattern decouples the client from the subsystem, allowing
    the client to interact with the system through the facade without
    needing to understand the underlying complexity.

Default Configuration:
    A Facade can offer a default configuration or behavior, simplifying
   common use cases.

Single Point of Access:
    It can provide a single entry point for accessing the subsystem,
    streamlining interactions.

Comparison with Abstract Factory:
    While an Abstract Factory provides an interface for creating families
    of related or dependent objects, a Facade is more like an API layer that
    can encompass creational, structural, and behavioral patterns.

Comparison with Mediator:
    The Facade is similar to the Mediator in that both abstract existing classes.
    However, while the Mediator centralizes communication between objects, the
    Facade simplifies the interface to a complex system.

Non-Intrusive:
    The Facade does not modify or interfere with the subsystems. The subsystems
    operate independently of the Facade, meaning they do not need to be aware of
    its existence.

Minimal Interface:
    A Facade typically represents a minimal interface, which could also
    be implemented as a Singleton to ensure a single point of access.

Optional Layer:
    The Facade is an optional layer that clients can use. The underlying
    subsystems do not need to be aware of the Facade, and the system can
    still function without it. Multiple Facades can be created for different
    audiences or purposes.

Usage:
------
Complex Systems:
    When dealing with a system that has many interacting components
    and is difficult to manage, the Facade pattern helps by offering
    a simpler, easier-to-use interface.

Layered Abstraction:
    When you want to layer your subsystems into an abstraction that
    hides the complexity and presents a more user-friendly interface.

"""

from unittest import TestCase, TextTestRunner


# ==========================================
#      classes of complex subsystems
# ==========================================
class SubSystemClassA():
    """A hypothetically complicated class"""

    @staticmethod
    def method():
        """A hypothetically complicated method"""
        return "subsystem_A"


class SubSystemClassB:
    """A hypothetically complicated class"""

    @staticmethod
    def method(value):
        "A hypothetically complicated method"
        return value


class SubSystemClassC:
    """A hypothetically complicated class"""


    @staticmethod
    def method(value):
        "A hypothetically complicated method"
        return value



# ==========================================
#              facade class
# ==========================================
class Facade:
    """A simplified facade offering
   the services of subsystems"""

    @staticmethod
    def sub_system_class_a():
        "Use the subsystems method"
        return SubSystemClassA().method()

    @staticmethod
    def sub_system_class_b(value):
        "Use the subsystems method"
        return SubSystemClassB().method(value)

    @staticmethod
    def method_c(value):
        """A simplified method"""
        return SubSystemClassC.method(value)

    @staticmethod
    def sub_system_class_c(value):
        "Use the subsystems method"
        return SubSystemClassC().method(value)


# ==========================================
#                   tests
# ==========================================
if __name__ == "__main__":

    class TestFacadePattern(TestCase):
        """A Test Class for the Facade Pattern"""

        def test_facade_pattern(self):
            """A test method to test the facade pattern"""

            facade = Facade()

            self.assertEqual(
                facade.sub_system_class_a(),
                SubSystemClassA.method()
            )

            self.assertEqual(
                facade.sub_system_class_b(124),
                SubSystemClassB.method(124)
            )

            self.assertEqual(
                facade.sub_system_class_c([1, 2, 3]),
                SubSystemClassC.method([1, 2, 3])
            )

    runner = TextTestRunner()
    runner.run(TestFacadePattern('test_facade_pattern'))
