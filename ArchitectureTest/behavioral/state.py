"""
Description:
------------
The State Pattern is a behavioral design pattern that allows an object
to alter its behavior when its internal state changes. This makes the
object appear to change its class. The key advantage is the reduction
in complex conditional statements within methods by delegating the
behavior to different state objects. This makes the code more
maintainable and easier to extend.

Key Features:
-------------
Dynamic Behavior Change:
    An object changes its behavior dynamically as its internal state changes,
    without needing to rewrite or use large conditional logic blocks.

Encapsulation of State:
    The details of state transitions and the behaviors associated with different
    states are encapsulated within separate state classes. The main object (context)
    delegates state-dependent behavior to these state objects.

Client Context Independence:
    The client interacting with the context object does not need to be aware
    of the state changes or how state-dependent behavior is implemented.
    The context forwards client requests to the current state object.

Comparison with Strategy Pattern:
    While the State Pattern is similar to the Strategy Pattern, they differ
    in their intent. The Strategy Pattern is used to select an algorithm at
    runtime, whereas the State Pattern is used to alter the object’s behavior
    when its state changes. In the State Pattern, the context is aware of the
    state and changes state based on the current context.

Usage:
------
Finite State Machines:
    When modeling objects that have a finite number of states, the State Pattern
    is ideal as it allows easy transitions and clear state management.

UI Elements:
    The State Pattern can be used in user interfaces where elements might change
    their behavior based on user interaction (e.g., buttons changing behavior based
    on whether they are enabled or disabled).

Game Development:
    In game development, characters or objects can change behavior (e.g., movement, attacks)
    based on their state (e.g., idle, walking, running, attacking).
"""

from abc import ABCMeta, abstractmethod
from unittest import TestCase, TextTestRunner
import random

class Context():
    """The Context class that
    will change its state"""

    def __init__(self):
        """Instantiates the Context class"""

        self.state_handles = [
            ConcreteStateA(),
            ConcreteStateB(),
            ConcreteStateC()
        ]

        self.handle = None

    def request(self):
        """A method of the state that dynamically changes which
        class it uses depending on the value of self.handle"""
        self.handle = self.state_handles[random.randint(0, 2)]
        return self.handle

    def change_state(self, state):
        self.state = state

class IState(metaclass=ABCMeta):
    """A State Interface"""

    @staticmethod
    @abstractmethod
    def __str__():
        """Set the default method"""

class ConcreteStateA(IState):
    """"A ConcreteState subclass"""

    def __str__(self):
        return "State A"

class ConcreteStateB(IState):
    """"A ConcreteState subclass"""

    def __str__(self):
        return "State B"

class ConcreteStateC(IState):
    """"A ConcreteState subclass"""

    def __str__(self):
        return "State C"

# ==========================================
#                   tests
# ==========================================
if __name__ == "__main__":

    class TestStatePattern(TestCase):
        """A Test Class for the State pattern"""

        def test_state(self):
            """A method to test the State class"""

            context = Context()
            print(context.request())
            print(context.request())
            print(context.request())
            print(context.request())


    runner = TextTestRunner()
    runner.run(TestStatePattern('test_state'))
