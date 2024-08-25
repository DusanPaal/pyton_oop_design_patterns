"""
Description:
------------
The Template Method Pattern is a behavioral design pattern that defines
the skeleton of an algorithm in a method, deferring some steps to subclasses.
This pattern allows subclasses to redefine certain steps of an algorithm
without changing its overall structure. The core idea is to outline an algorithm
in an abstract class, which contains a template method composed of abstract
methods and hook methods.

Abstract Methods:
    These are the methods that must be implemented by the subclasses.
    They represent the steps of the algorithm that vary across different
    implementations.

Hook Methods:
    These are optional methods that can be overridden by subclasses
    to provide additional behavior. They typically have default or empty
    implementations in the abstract class.

    The abstract class serves as the template, providing the framework for the algorithm
    while allowing subclasses the flexibility to customize certain steps. This approach
    promotes code reuse and enforces a consistent algorithm structure across different
    implementations.

Key Features:
-------------
Algorithm Skeleton:
    The abstract class defines a template method that outlines the structure of an algorithm.
    This method orchestrates the sequence of steps, some of which are implemented in the abstract
    class and others in the subclasses.

Abstract Methods:
    These are the essential parts of the algorithm that must be provided by subclasses.
    They ensure that each subclass can tailor the algorithm to its specific needs.

Hook Methods:
    These methods offer optional customization points. Subclasses can choose to override
    these methods to alter the algorithm's behavior or leave them as-is if the default
    behavior is sufficient.

Code Reuse:
    By defining the common algorithm in the abstract class and allowing specific steps
    to be customized, the Template Method Pattern encourages code reuse and reduces redundancy.

Reduction of Conditional Logic:
    If a class has many conditional statements to determine behavior, the Template Method Pattern
    can help refactor the code by moving those conditions into subclass implementations.

Usage:
------
Framework Design:
    The Template Method Pattern is particularly useful in frameworks where
    a general process needs to be defined, but specific details can vary
    depending on the application. For example, a framework for processing
    data files might define the general process (opening, reading, processing,
    closing files) in an abstract class, while allowing different file types
    to provide their own implementations of the processing step.

Code Refactoring:
    When you find that a class contains multiple conditional statements that
    switch between different behaviors, the Template Method Pattern can be
    used to refactor the code, pushing the specific behaviors into subclasses
    and simplifying the overall logic.

Library Classes:
    The pattern is commonly used to extract and reuse common behaviors in
    libraries, allowing different subclasses to customize behavior without
    altering the core algorithm.

"""

from abc import ABCMeta, abstractmethod
from unittest import TestCase, TextTestRunner


class AbstractClass(metaclass=ABCMeta):
    """The Abstract Class"""

    @staticmethod
    def operation_01():
        """Hooks are normally empty in the abstract class. The
        implementing class can optionally override providing a custom
        implementation"""

    @staticmethod
    def operation_02():
        """Hooks can also contain default behavior and can be optionally
        overridden"""
        print("Step Three is a hook that prints this line by default.")

    @staticmethod
    @abstractmethod
    def operation_03():
        """An abstract method that must be overridden in the implementing
        class. It has been given `@abstractmethod` decorator so that
        pylint shows the error."""

    @classmethod
    def template_method(cls):
        """This is the template method that the subclass will call.
        The subclass (implementing class) doesn't need to override this
        method since it has would have already optionally overridden
        the following methods with its own implementations"""

        cls.operation_01()
        cls.operation_02()
        cls.operation_03()

class ConcreteClassA(AbstractClass):
    """A concrete class that only overrides step three"""

    @staticmethod
    def operation_03():
        """Overrides the hook method operation_03()"""
        print("Class A : Step Three (overridden)")

class ConcreteClassB(AbstractClass):
    """A concrete class that only
    overrides steps one, two and three"""

    @staticmethod
    def operation_01():
        """Overrides the hook method operation_01()"""
        print("Class B : Step One (overridden)")

    @staticmethod
    def operation_02():
        """Overrides the hook method operation_02()"""
        print("Class B : Step Two (overridden)")

    @staticmethod
    def operation_03():
        """Overrides the abstract method operation_03()"""
        print("Class B : Step Three (overridden)")


# ==========================================
#                   tests
# ==========================================
if __name__ == "__main__":

    class TestTemplateMethodPattern(TestCase):
        """A Test Class for the Template Method pattern"""

        def test_template_metod(self):
            """A method to test the  Template Method class"""

            class_a = ConcreteClassA()
            class_a.template_method()

            class_b = ConcreteClassB()
            class_b.template_method()


    runner = TextTestRunner()
    runner.run(TestTemplateMethodPattern('test_template_metod'))