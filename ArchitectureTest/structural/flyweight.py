# Description.
# ------------
# The Flyweight pattern describes how to share objects rather than
# creating thousands of almost repeated objects unnecessarily.
#
# Useful when:
# ------------
# - saving memory is a priority
#y
# Key features:
# ------------
# - Intrinsic values are stored internally in the Flyweight
# - Extrinsic values are passed to the Flyweight and customise it depending on the context
# - Implementing the flyweight is a balance between storing all objects in memory, versus
#   storing small unique parts in memory, and potentially calculating extrinsic values in
#   the context objects
# - The flyweight reduces memory footprint because it shares objects and allows the possibility
#   of dynamically creating extrinsic attributes
# - The offset is that extra CPU may be required during calculating and passing extrinsic values
#   to the flyweights.


from abc import ABCMeta, abstractmethod
from unittest import TestCase, TextTestRunner


class IFlyweight(metaclass=ABCMeta):
    """The flyweight interface"""
    # nothing to implement


class Flyweight(IFlyweight):
    """The Concrete Flyweight"""

    def __init__(self, code: int) -> None:
        self.code = code

class FlyweightFactory():
    """Creating the FlyweightFactory as a singleton"""

    _flyweights: dict[int, Flyweight] = {}

    def __new__(cls):
        return cls

    @classmethod
    def get_flyweight(cls, code: int) -> Flyweight:
        """"Get a flyweight based on a code"""

        if code not in cls._flyweights:
            cls._flyweights[code] = Flyweight(code)

        return cls._flyweights[code]

    @classmethod
    def get_count(cls) -> int:
        """Return the number of flyweights in the cache"""
        return len(cls._flyweights)

class Context:
    """An example context that holds
    references to the flyweights in a
    particular order and converts the
    code to an ascii letter."""

    def __init__(self, codes: str) -> None:
        self.codes = list(codes)

    def ouptut(self):
        """The context specific output that uses flyweights"""

        ret = ""

        for code in self.codes:
            ret = ret + FlyweightFactory.get_flyweight(code).code

        return ret


# ==========================================
#                   tests
# ==========================================
if __name__ == "__main__":

    class TestFlyweightPattern(TestCase):
        """A Test Class for the Flyweight Pattern"""

        def test_flyweight_pattern(self):
            """A test method to test the flyweight pattern"""

            context = Context("abracadabra")
            output = context.ouptut()

            self.assertEqual(output, "abracadabra")
            self.assertEqual(FlyweightFactory.get_count(), 5)

    runner = TextTestRunner()
    runner.run(TestFlyweightPattern('test_flyweight_pattern'))