# Description.
# ------------
# The Facade pattern is a structural pattern that provides
# a simplified interface to a complex system, consisting of
# one or more subsystems. It is a higher-level interface that
# makes the subsystem easier to use.
#
# Useful when:
# ------------
# - the system id complex has many components and interactions and is difficult to understand or change,
#   and you want to layer your subsystems into an abstraction that is easier to understand.
#
# Key features:
# ------------
# - provides a simple interface to a complex system
# - hides the complexity of the system from the client
# - decouples the client from the system
# - can provide a default configuration or behavior
# - can provide a single point of access to a subsystem
# - abstract Factory and Facade can be considered very similar. An Abstract Factory is about
#   creating in interface over several creational classes of similar objects, whereas the Facade is
#   more like an API layer over many creational, structural and/or behavioral patterns.
# - The Mediator is similar to the Facade in the way that it abstracts existing classes.
# - The Facade is not intended to modify, load balance or apply any extra logic. A subsystem does not need to
#   consider that existence of the facade, it would still work without it.
# - A Facade is a minimal interface that could also be implemented as a Singleton.
# - a Facade is an optional layer that does not alter the subsystem. The subsystem does not need
#   to know about the Facade, and could even be used by many other facades created for different
#   audiences.

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
