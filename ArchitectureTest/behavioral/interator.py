"""
Description:
------------
The Iterator pattern allows clients to traverse a collection of objects (aggregates)
without needing to understand the underlying data structures or internal representations.

Key Features:
------------
Traversal Methods:
    - next(): Returns the next object in the collection.
    - has_next(): Returns a bool indicating whether the
                  iterator has reached the end of the collection.
Usage:
------
- Built-in Support:
    Iterators are natively supported in Python,
    often negating the need to create custom classes.

- When to Use:
    Use an iterator when you need to traverse a collection
    or generate a series of objects dynamically.

- Minimum Requirements:
    An iterator must at least have a next method
    to return the next object in the sequence.

- Optional Helpers:
    Implement a helper function like has_next()
    to check if the iterator has more items,
    especially useful in loops.

- Python-Specific Options:
    In Python, you can use the iter() method with
    a sentinel value to signal the end of iteration.
    For this, the iterator object must be callable,
    typically by setting its __call__() method to
    reference its next method.
"""

from abc import ABCMeta, abstractmethod
from unittest import TestCase, TextTestRunner

class IIterator(metaclass=ABCMeta):
    """An Iterator Interface"""

    @staticmethod
    @abstractmethod
    def next() -> object:
       """Returns the next
       object in the collection"""

    @staticmethod
    @abstractmethod
    def has_next() -> bool:
        """Returns Boolean whether
        the iteration has reached
        the end of collection."""

class Iterable(IIterator):
    """The Iterator class, that
    traverses the collection"""

    def __init__(self, aggregates):
        self.aggregates = aggregates
        self.index = 0

    def next(self) -> object:
        """Returns the next object in the collection"""
        if self.has_next():
            item = self.aggregates[self.index]
            self.index += 1
            return item
        return None

    def has_next(self) -> bool:
        """Returns a Boolean indicating if the
        Iterable is at the end of the iteration"""
        return self.index < len(self.aggregates)


class IAggregate(metaclass=ABCMeta):
    """An interface that the
    aggregates should implement"""

    @staticmethod
    @abstractmethod
    def method():
        """A method to implement"""

class Aggregate(IAggregate):
    """A concrete object"""

    def __init__(self, name):
        """Creates an instance of
        the concrete the Aggregate"""
        self.name = name

    def method():
        print("Method has been invoked")


# ==========================================
#                   tests
# ==========================================
if __name__ == "__main__":

    class TestIteratorPattern(TestCase):
        """A Test Class for the Iterator pattern"""

        def test_iterator(self):
            """A method to test the Iterator class"""

            aggregate1 = Aggregate("Aggregate 1")
            aggregate2 = Aggregate("Aggregate 2")
            aggregate3 = Aggregate("Aggregate 3")

            collection = [aggregate1, aggregate2, aggregate3]
            iterator = Iterable(collection)

            self.assertTrue(iterator.has_next())
            self.assertEqual(iterator.next().name, "Aggregate 1")

            self.assertTrue(iterator.has_next())
            self.assertEqual(iterator.next().name, "Aggregate 2")

            self.assertTrue(iterator.has_next())
            self.assertEqual(iterator.next().name, "Aggregate 3")


    runner = TextTestRunner()
    runner.run(TestIteratorPattern('test_iterator'))