"""
Description:
------------
The Mediator pattern centralizes communication between objects,
allowing them to interact indirectly through a mediator rather
than directly with each other. As systems grow in complexity,
managing direct communication between components becomes challenging.
The Mediator pattern helps simplify and manage these interactions
by centralizing and coordinating communication.

Key Features:
------------
Centralized Communication:
    The Mediator replaces many-to-many interactions between classes
    and processes with a one-to-many structure, where the Mediator
    handles all communications.

Shared Object Management:
    The pattern encourages the use of shared objects, which
    can be centrally managed and synchronized by the Mediator.

Abstraction and Simplification:
    By creating an abstraction layer, the Mediator pattern
    makes the system easier to understand and manage.

Bidirectional Data Transactions:
    Unlike the Facade pattern, which often simplifies interactions, the
    Mediator pattern facilitates two-way communication between components.

Usage:
------
When to Use:
    Implement the Mediator pattern when direct communication between
    components becomes too complex to manage, and centralizing this
    communication would simplify the system's structure.

Related Patterns:
    The Mediator pattern is often compared to the Facade pattern but
    is distinct in its ability to handle bidirectional communication.
    It may also work in tandem with the Observer pattern to manage
    notifications among components.
"""

from abc import ABCMeta, abstractmethod
from unittest import TestCase, TextTestRunner

class IMediator(metaclass=ABCMeta):
    """The Mediator interface indicating
    all the methods to implement"""

    @staticmethod
    @abstractmethod
    def colleague_01_method() -> object:
        """Method to call when colleague1
        needs to communicate with colleague2"""

    @staticmethod
    @abstractmethod
    def colleague_02_method() -> object:
        """Method to call when colleague2
        needs to communicate with colleague1"""

class Mediator(IMediator):
    """The Mediator concrete Class"""

    def __init__(self):
        """Instantiates the concrete Mediator"""
        self.colleague_01 = Colleague1()
        self.colleague_02 = Colleague2()

    def colleague_01_method(self):
        """Method to call when colleague 01
        needs to communicate with colleague2"""
        return self.colleague_01.colleague_01_method()

    def colleague_02_method(self):
        """Method to call when colleague 02
        needs to communicate with colleague1"""
        return self.colleague_02.colleague_02_method()

class Colleague1(IMediator):
    """This Colleague calls the
    Colleague 02 via the Mediator"""

    def colleague_01_method(self):
        """The concrete method implemented at Colleague 01"""
        return "Resonse form the Colleague 01"

    def colleague_02_method(self):
        """not implemented"""
        raise NotImplementedError(
            "Method colleague_02_method() not implemented!")

class Colleague2(IMediator):
    """This Colleague calls the
    Colleague 01 via the Mediator"""

    def colleague_01_method(self):
        """not implemented"""
        raise NotImplementedError(
            "Method colleague_01_method() not implemented!")

    def colleague_02_method(self):
        """The concrete method implemented at Colleague 02"""
        return "Resonse form the Colleague 02"


# ==========================================
#                   tests
# ==========================================
if __name__ == "__main__":

    class TestMediatorPattern(TestCase):
        """A Test Class for the Iterator pattern"""

        def test_mediator(self):
            """A method to test the Mediator class"""

            mediator = Mediator()
            self.assertEqual(mediator.colleague_01_method(), "Resonse form the Colleague 01")
            self.assertEqual(mediator.colleague_02_method(), "Resonse form the Colleague 02")


    runner = TextTestRunner()
    runner.run(TestMediatorPattern('test_mediator'))