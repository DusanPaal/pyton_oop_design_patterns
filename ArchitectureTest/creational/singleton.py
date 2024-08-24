# Description:
# ------------
# The Singleton can be accessible globally, but it is not a global variable. It is a class that can be
# instanced at any time, but after it is first instanced, any new instances will point to the same instance
# as the first.
# For a class to behave as a Singleton, it should not contain any references to self but use static
# variables, static methods and/or class methods
# in order to work, the class level variables must be used as well as static or class mehtods
# - cls is a reference to the class
# - self is a reference to the instance of the class
# _new_ gets called before _init_, and has access to class level variables
#_init_ references self that is created when the class is instantiated ätherefore, must be avoided in a Singleton)
# By using _new_, and returning a reference to cls, we can force the class to act as a singleton


# To be a Singleton, there must only be one copy of the Singleton, no matter how many times, or
# in which class it was instantiated.
# You want the attributes or methods to be globally accessible across your application, so that
# other classes may be able to use the Singleton.
# You can use Singletons in other classes, as I did with the leaderboard, and they will all use the
# same Singleton regardless.
# You want controlled access to a sole instance.
# For a class to act as a singleton, it should not contain any references to self .
# Useful when:
# ------------
# - onl one instance of a class is needed in the program
# - the instance of a class should be easily accessible and extensible
#
# Key features:
# ------------
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
