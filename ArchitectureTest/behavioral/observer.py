"""
Description:
------------
The Observer pattern is a software design pattern where an object, known as the Subject
(or Observable), maintains a list of dependents, called Observers. The Subject automatically
notifies these Observers of any internal state changes by invoking one of their methods.
This pattern follows the publish/subscribe model, where subscribers register with a publisher
and are notified as needed.

Key Features:
-------------
State Consistency:
    Observers maintain a state that should align with the Subject
    but only store what is necessary for their specific functions.

Flexibility in Use:
    The Observer pattern allows for independent variation of Subjects
    and Observers, enabling reuse without requiring changes to either party.

Push/Pull Mechanisms:
    The pattern can function as a push model, where the Subject pushes updates
    to Observers, or as a pull model, where Observers request updates from the Subject.
    Each approach has its own pros and cons, depending on the system's needs for
    real-time updates versus ease of management and reliability.

Usage:
------
Application in Layers:
    A common use case is between the application and presentation layers,
    where the application (Subject) manages data and updates multiple
    presentation components (Observers) when the data changes. For example,
    in a televised cricket game, a score change would automatically update
    all web browsers, mobile apps, and TV graphics simultaneously.

Model-View-Controller (MVC):
    The Observer pattern fits well within the MVC architecture,
    where the View (Observer) can subscribe to the Model, which
    in turn subscribes to the Controller.

Scalability:
    The pattern is suitable for systems of any size and can be applied
    across different layers or even within a single layer to add abstraction.

Considerations
    The pattern is used when a change in one object necessitates changes in others,
    without knowing in advance how many objects need updating. The decision to use
    either the push or pull mechanism is based on the system’s requirements for
    real-time updates versus handling delays and managing resource use.
"""

from abc import ABCMeta, abstractmethod
from unittest import TestCase, TextTestRunner

class IObservable(metaclass=ABCMeta):
    """The Observable interface, that
    all subjects will implement"""

    @staticmethod
    @abstractmethod
    def subscribe(self, observer):
        """The method to add an observer to the subject"""

    @staticmethod
    @abstractmethod
    def unsubscribe(self, observer):
        """The method to remove an observer from the subject"""

    @staticmethod
    @abstractmethod
    def notify(self):
        """The method to notify all observers"""

class Subject(IObservable):
    """The concrete subject class that
    will notify all observers"""

    def __init__(self):
        self._observers = set()

    def subscribe(self, observer):
        """Add an observer to the list"""
        print(f"Adding observer {observer.name} ...")
        self._observers.add(observer)

    def unsubscribe(self, observer):
        """Remove an observer from the list"""
        print(f"Removing observer {observer.name} ...")
        self._observers.remove(observer)

    def notify(self, *args):
        """Notify all observers"""
        for observer in self._observers:
            observer.update(*args)

class IObserver(metaclass=ABCMeta):
    """The Observer interface, that
    all observers will implement"""

    @staticmethod
    @abstractmethod
    def update(self):
        """The method to update the observer"""

class Observer(IObserver):
    """The concrete observer class that
    will be notified by the subject"""

    def __init__(self, observable, name):
        self.name = name
        observable.subscribe(self)
        print("Observer created: '{self.name}'")

    def update(self, *args):
        """Update the observer"""
        print(f"Observer '{self.name}' id:{id(self)} received {args}")

# ==========================================
#                   tests
# ==========================================
if __name__ == "__main__":

    class TestObserverPattern(TestCase):
        """A Test Class for the Observer pattern"""

        def test_observer(self):
            """A method to test the Observer class"""

            subject = Subject()
            observer_a = Observer(subject, name = "A")
            observer_b = Observer(subject, name = "B")

            self.assertEqual(len(subject._observers), 2)
            self.assertEqual(observer_a.name, "A")
            self.assertEqual(observer_b.name, "B")

            subject.notify("First notification", [1, 2, 3])

            subject.unsubscribe(observer_b)
            subject.notify("Second notification", {"A": 1, "B": 2, "C": 3})

    runner = TextTestRunner()
    runner.run(TestObserverPattern('test_observer'))
