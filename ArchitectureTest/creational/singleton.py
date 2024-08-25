"""
Description:
------------
The Singleton Pattern ensures that a class has only one instance
and provides a global point of access to that instance. It is designed
to control the instantiation of a class so that only one instance
exists throughout the application.

Key features:
-------------
Global Access Without Global Variables:
    Unlike global variables, a Singleton is accessed through its class
    methods or properties, providing a controlled global access point.

Static Methods and Variables:
    The Singleton Pattern uses static variables and methods to store
    and manage the single instance. This ensures that no matter how
    many times the Singleton class is accessed or instantiated, only
    one instance exists.

Instance Creation Control:
    The Singleton Pattern typically overrides the __new__ method (in Python)
    or similar methods in other languages to ensure that only one instance is
    created. The __init__() method is not used for this purpose, as __new__()
    is responsible for creating the instance.

No Self References:
    In the Singleton Pattern, instance methods (which use self) are generally
    avoided for managing the singleton instance. Instead, static methods or
    class methods (using cls in Python) are used.

Usage:
------
Single Instance Requirement:
    When you need only one instance of a class to coordinate actions
    across the system. For example, a configuration manager or a logging
    service might benefit from being a Singleton.

Global Access:
    When you want to provide a single, globally accessible instance
    that can be used throughout your application.

Controlled Access:
    When you need to control access to a sole instance,
    ensuring that all parts of your application use the same object.
"""

import copy
from unittest import TestCase, TextTestRunner

class Singleton():
    """A class that can be instanced only once"""

    value = []

    def __new__(cls):
        return cls

    @staticmethod
    def static_method():
        """Use @staticmethod if no inner variables required"""

    @classmethod
    def class_method(cls):
        """Use @classmethod to access class level variables"""
        print(cls.value)


# ==========================================
#                   tests
# ==========================================
if __name__ == "__main__":

    class TestSingletonPattern(TestCase):
        """A Test Class for the Factory Pattern"""

        def test_singleton_pattern(self):
            """A test method to test the singleton pattern"""

            sngl_a = Singleton()
            sngl_b = copy.deepcopy(sngl_a)
            sngl_c = Singleton()

            # all 3 instances should point to the same object
            self.assertEqual(sngl_a, sngl_c)
            self.assertEqual(sngl_b, sngl_c)

    runner = TextTestRunner()
    runner.run(TestSingletonPattern('test_singleton_pattern'))
