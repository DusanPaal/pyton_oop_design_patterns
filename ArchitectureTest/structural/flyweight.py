"""
Description:
------------
The Flyweight Pattern is a structural design pattern that focuses on minimizing
memory usage by sharing objects instead of creating multiple instances of objects
that are almost identical. It is especially useful in situations where a large
number of similar objects are needed.

Key features:
------------
1. Intrinsic vs. Extrinsic Values:

    1.1 Intrinsic Values:
        These are the invariant (unchanging) parts of the object
        that are shared among all instances. They are stored
        internally within the Flyweight.

    1.2 Extrinsic Values:
        These are the varying parts of the object that can be
        passed in from outside to customize the Flyweight based
        on the context. They are not stored within the Flyweight
        but provided by the client when needed.

2. Memory Footprint Reduction:
    By sharing common parts of objects (intrinsic values) and only
    varying what’s necessary (extrinsic values), the Flyweight Pattern
    significantly reduces the memory footprint.

3. Trade-offs:

    3.1 Memory vs. CPU Usage:
        Implementing the Flyweight Pattern involves a trade-off
        between saving memory and potentially increasing CPU usage.
        The pattern reduces memory consumption but may require
        additional computation to manage extrinsic values.

    3.1 Balancing Storage:
        It requires careful balancing between what is stored internally
        (intrinsic) and what is passed or computed externally (extrinsic).
        The goal is to store only the unique, essential parts of objects
        in memory and dynamically calculate or pass other parts as needed.

Usage:
------
Memory Optimization:
    The Flyweight Pattern is ideal when memory usage is a priority, and you need
    to reduce the number of objects created in a system by sharing common parts
    of object state.
"""

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