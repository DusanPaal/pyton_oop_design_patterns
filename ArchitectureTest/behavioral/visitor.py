"""
Description:
------------
The Visitor Pattern is a behavioral design pattern that enables you to add new
operations to a complex object structure without modifying the objects themselves.
This pattern is particularly useful when working with an object hierarchy, like
a Composite structure, where the objects may be varied and complex.

In essence, the Visitor Pattern allows you to separate an algorithm from the object
structure it operates on. The objects in the hierarchy implement a Visitor interface,
which includes an accept() method. This method allows a Visitor object to traverse
the hierarchy and perform operations on the elements without altering their classes.

The primary advantage of the Visitor Pattern is that it enables you to add new
functionality to the object structure without changing the objects classes,
which is crucial in maintaining the integrity of the application as it grows
and evolves.

For example, if you have a hierarchical structure of objects representing parts
of a document (e.g., chapters, sections, paragraphs), you can use the Visitor Pattern
to define different operations (like exporting to different formats) without changing
the document structure itself.

Key Features:
-------------
Separation of Concerns:
    The Visitor Pattern separates the algorithm from the object structure,
    allowing you to define new operations independently of the objects on
    which they operate.

Extensibility:
    You can add new operations to a complex object hierarchy without modifying
    the existing object classes, which enhances maintainability and scalability.

Single Responsibility Principle (SRP):
    By implementing the custom operations in a separate visitor class, the object
    classes remain focused on their primary responsibilities, conforming to the
    Single Responsibility Principle.

Flexibility in Operations:
    The Visitor Pattern allows you to define operations that can work across
    different types of objects in a hierarchy, making it easier to implement
    cross-cutting concerns.

Usage:
------
Complex Object Structures:
    Use the Visitor Pattern when you have an object hierarchy, such as a Composite
    structure, where you need to perform various operations on elements without
    modifying their classes.

Adding New Operations:
    When you anticipate the need to add new operations to objects without changing
    their structure, the Visitor Pattern provides a clean solution.

Maintaining SRP:
    The Visitor Pattern is ideal for scenarios where you want to keep the responsibilities
    of your classes focused by moving additional operations into separate visitor classes.

Document Processing:
    This pattern is particularly useful in applications that involve document processing,
    where you might need to output different versions or formats of a document, each
    requiring distinct operations.
"""

from abc import ABCMeta, abstractmethod
from unittest import TestCase, TextTestRunner


class IVisitor(metaclass=ABCMeta):
    """An interface that custom Visitors should implement"""

    @staticmethod
    @abstractmethod
    def visit(element):
        """Visitors visit Elements/Objects within the application"""


class IVisitable(metaclass=ABCMeta):
    """An interface the concrete objects should implement that allows
    the visitor to traverse a hierarchical structure of objects.
    """

    @staticmethod
    @abstractmethod
    def accept(visitor):
        """The Visitor traverses and accesses each object through this method"""


class Element(IVisitable):
    """An Object that can be part of any hierarchy"""

    def __init__(self, name, value, parent=None):
        """Instantiates the Element class"""

        self.name = name
        self.value = value
        self.elements = set()

        if parent:
            parent.elements.add(self)


class PrintElementNamesVisitor(IVisitor):
    """Create a visitor that prints the Element names"""

    @staticmethod
    def visit(element):
        print(element.name)


class CalculateElementsTotalsVisitor(IVisitor):
    """Create a visitor that calculates the total of all elements"""

    total_value = 0

    @staticmethod
    def visit(cls, element):
        cls.total_value += element.value
        return cls.total_value


# ==========================================
#                   tests
# ==========================================
if __name__ == "__main__":

    class TestVisitorPattern(TestCase):
        """A Test Class for the Visitor pattern"""

        def test_visitor(self):
            """A method to test the Visitor class"""

            # The Client - creating an example object hierarchy
            element_a = Element("A", 100)
            element_b = Element("B", 200, element_a)
            element_c = Element("C", 300, element_a)
            element_d = Element("D", 400, element_c)

            # Now rather than changing the Element class to support
            # custom operations, we can utilize the accept method that
            # was implemented in the Element class because of the addition
            # of the IVisitable interface
            element_a.accept(PrintElementNamesVisitor)

            # Using the CalculateElementTotalsVisitor to traverse the
            # object hierarchy
            total = CalculateElementsTotalsVisitor()
            element_a.accept(CalculateElementsTotalsVisitor)
            print(total.total_value)

    runner = TextTestRunner()
    runner.run(TestVisitorPattern('test_visitor'))


class CalculateElementsTotalsVisitor(IVisitor):
    """Create a visitor that calculates the total of all elements"""

    total_value = 0

    @staticmethod
    def visit(cls, element):
        cls.total_value += element.value
        return cls.total_value


# ==========================================
#                   tests
# ==========================================
if __name__ == "__main__":

    class TestVisitorPattern(TestCase):
        """A Test Class for the Visitor pattern"""

        def test_visitor(self):
            """A method to test the Visitor class"""

            # The Client - creating an example object hierarchy
            element_a = Element("A", 100)
            element_b = Element("B", 200, element_a)
            element_c = Element("C", 300, element_a)
            element_d = Element("D", 400, element_c)

            # Now rather than changing the Element class to support
            # custom operations, we can utilise the accept method that
            # was implemented in the Element class because of the addition
            # of the IVisitable interface
            element_a.accept(PrintElementNamesVisitor)

            # Using the CalculateElementTotalsVisitor to traverse the
            # object hierarchy
            total = CalculateElementsTotalsVisitor()
            element_a.accept(CalculateElementsTotalsVisitor)
            print(total.total_value)

    runner = TextTestRunner()
    runner.run(TestVisitorPattern('test_visitor'))
