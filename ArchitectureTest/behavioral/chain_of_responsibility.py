"""
Description:
------------
The Chain of Responsibility is a behavioral design pattern that promotes loose
coupling by passing an object through a sequence of handlers, known as successors.
Each successor decides, based on a specific logic, whether to process the object
or pass it to the next handler in the chain.

Key Features:
-------------
Independent Object Handling:
    The object being passed does not know which successor will handle it.
    Each successor may or may not process the object before passing it
    along the chain.

Common Interface:
    Successors implement a common interface, allowing them
    to operate independently and be reordered or used recursively.

Dynamic Chain:
    The sequence of successors is typically determined at runtime,
    though it can be hardcoded. Each successor must comply with the
    interface that enables the object to be received and forwarded.

Complete Propagation:
    The object continues through the chain until it has been fully
    processed.

Usage:
------
- Common applications include user wizards or dynamic questionnaires.

- The Chain of Responsibility pattern is often used in conjunction with
  the Composite pattern due to their shared focus on hierarchy and reordering
  flexibility. While the Composite pattern relies on external processes to manage
  parent-child relationships, the Chain of Responsibility pattern internally
  determines the next successor dynamically.

- The chain can be either dynamically created at runtime or set by default,
  with potential adjustments during execution.
"""

import random
from abc import ABCMeta, abstractmethod
from unittest import TestCase, TextTestRunner

class IHandler(metaclass=ABCMeta):
    """The Handler interface, that
    all successors will implement"""

    @staticmethod
    @abstractmethod
    def handle(payload):
        """The required handling method
        that all successors will use"""

class Successor1(IHandler):
    """A handler 01, that runs the
    command on the designated receiver"""

    @staticmethod
    def handle(payload):
        """The concrete handling method"""

        print(f"Successor 1 payload = {payload}")
        test = random.randint(1, 2)

        if test == 1:
            payload = payload + 1
            payload = Successor1().handle(payload)
        if test == 2:
            payload = payload - 1
            payload = Successor2().handle(payload)
        return payload

class Successor2(IHandler):
    """A handler 02, that runs the
    command on the designated receiver"""

    @staticmethod
    def handle(payload):
        """The concrete handling method"""

        print(f"Successor 2 payload = {payload}")
        test = random.randint(1, 3)

        if test == 1:
            payload = payload * 2
            payload = Successor1().handle(payload)
        if test == 2:
            payload = payload / 2
            payload = Successor2().handle(payload)

        return payload

class Chain:
    """A chain with a default first successor"""

    @staticmethod
    def start(payload):
        """Setting the first successor
        that will modify the payload"""
        return Successor1().handle(payload)


# ==========================================
#                   tests
# ==========================================
if __name__ == "__main__":

    class TestChainOfResponsibilityPattern(TestCase):
        """A Test Class for the Chain of Responsibility pattern"""

        def test_chor(self):
            """A method to test the Chain of Responsibility class"""

            out = Chain().start(payload = 1)
            print(f"Finished result = {out}")

    runner = TextTestRunner()
    runner.run(TestChainOfResponsibilityPattern('test_chor'))