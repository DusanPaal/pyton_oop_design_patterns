"""
Description:
------------
The Strategy Pattern is a behavioral design pattern that allows a client to choose
which algorithm to execute at runtime without altering the context in which the
algorithm is used. Unlike the State Pattern, where the context’s behavior changes
as its state changes, the Strategy Pattern keeps the context's state unchanged while
dynamically selecting from a variety of algorithms to perform a specific task.

In this pattern, each algorithm is encapsulated within a class that implements
a specific strategy interface. The client selects the desired algorithm, which
is then passed to the context to be executed. The context is unaware of the
specific details of the algorithm and relies on the strategy interface to process
the data.

For example, consider an application that sorts data. The user interface can
provide a drop-down menu allowing the user to select different sorting algorithms
the (e.g., quicksort, mergesort, bubblesort). Upon user selection, the reference to
chosen algorithm is passed to the context, which processes the data using this algorithm
without altering the state of the context.

Key Features:
-------------
Algorithm Substitution:
    The Strategy Pattern allows for the substitution of algorithms at runtime,
    giving the client the flexibility to choose from different implementations
    that accomplish the same task.

Encapsulation of Algorithms:
    Each algorithm is encapsulated in its own class, implementing a common interface.
    This decouples the algorithm’s implementation from the context, promoting flexibility
    and reusability.

Separation of Concerns:
    The Strategy Pattern separates the selection of an algorithm from the context’s responsibility.
    The context only knows about the strategy interface and doesn't need to know the specifics of
    each algorithm.

Comparison with State Pattern:
    While the State Pattern changes the context's behavior based on its state, the Strategy Pattern
    focuses on choosing among multiple algorithms without changing the state of the context.
    The decision to use a particular strategy is made externally by the client and can be altered
    at any time without affecting the context's state.

Usage:
------
Data Processing:
    The Strategy Pattern is ideal for scenarios where an application needs to process data using
    different algorithms, such as sorting, filtering, or compression. Users can switch between
    different strategies depending on the requirements.

Software Plugins:
    This pattern is useful for implementing plugins in software applications. Each plugin can be
    treated as a strategy, allowing the application to dynamically load and execute different
    functionalities without changing the core logic.

Payment Processing Systems:
    In e-commerce applications, different payment methods (e.g., credit card, PayPal, cryptocurrency)
    can be implemented as strategies, allowing the user to choose their preferred payment method at checkout.

"""

from abc import abstractmethod, ABCMeta
from unittest import TestCase, TextTestRunner

class Context:
    """The Context class whose behaviou will change"""

    @staticmethod
    def request(strategy):
        """The request method that
        will run the chosen strategy"""
        return strategy().execute()

class IStrategy(metaclass=ABCMeta):
    """The Strategy Interface"""

    @staticmethod
    @abstractmethod
    def execute(self):
        """The execute method that
        will be overridden by concrete
        strategies"""

class ConcreteStrategyA(IStrategy):
    """A Concrete Strategy Subclass"""

    def execute(self):
        return "Algorithm A"

class ConcreteStrategyB(IStrategy):
    """A Concrete Strategy Subclass"""

    def execute(self):
        return "Algorithm B"

class ConcreteStrategyC(IStrategy):
    """A Concrete Strategy Subclass"""

    def execute(self):
        return "Algorithm C"


# ==========================================
#                   tests
# ==========================================
if __name__ == "__main__":

    class TestStrategyPattern(TestCase):
        """A Test Class for the Strategy pattern"""

        def test_strategy(self):
            """A method to test the Strategy class"""

            context = Context()
            result = context.request(ConcreteStrategyA)
            self.assertEqual(result, "Algorithm A")

            result =context.request(ConcreteStrategyB)
            self.assertEqual(result, "Algorithm B")

            result =context.request(ConcreteStrategyC)
            self.assertEqual(result, "Algorithm C")

    runner = TextTestRunner()
    runner.run(TestStrategyPattern('test_strategy'))
