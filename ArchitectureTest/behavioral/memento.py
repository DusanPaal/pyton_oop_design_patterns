"""
Description:
------------
The Memento pattern is used to save and restore an object's state at different points
in its lifecycle. This is particularly useful for features like auto-save in a document
editor or saving a player's progress in a game. Unlike the Command pattern, which re-executes
commands to revert changes, the Memento pattern allows you to completely replace the object's
state by retrieving it from a stored snapshot.

Key Features:
-------------
Selective State Saving:
    A new Memento doesn't need to be created each time the state
    changes—only when necessary, such as during periodic backups

Storage and Retrieval:
    Mementos can be stored in memory or externally, with the Caretaker managing
    the complexities of saving and retrieving Mementos from the Originator.

Integration with Command pattern:
    For fine-grained state changes and managing UNDO/REDO operations,
    the Command pattern can be used in tandem with Mementos, or command
    history can be saved in a Memento for later replay.

State Copying Considerations:
    The Memento can record and restore either the entire state or partial states,
    depending on the requirement. Shallow versus deep copying should be kept in mind,
    as a mix of both may be required in complex projec

Usage:
------
- when object states need to be saved and restored (Undo/Redo Functionality),
  especially in applications that require the ability to revert to previous
  states, like document editors or games.
"""

from unittest import TestCase, TextTestRunner

class Memento():
    """Memento class to store the state of an object"""

    def __init__(self, state) -> None:
        self.state = state

class Originator():
    """The Object in the application whose state changes"""

    def __init__(self) -> None:
        self._state = ""

    @property
    def state(self):
        """A `getter` for the objects state"""
        return self._state

    @state.setter
    def state(self, state):
        print(f"Originator: Setting state to `{state}`")
        self._state = state

    @property
    def memento(self):
        """A `getter` for the objects
        state but packaged as a Memento"""

        print("Originator: Providing Memento of state to caretaker.")
        return Memento(self._state)

    @memento.setter
    def memento(self, memento):
        """A `setter` for the objects state
        but packaged as a Memento"""

        self._state = memento.state

        print(
            "Originator: State after restoring "
            f" from Memento: `{self._state}`"
        )

class Caretaker():
    """Guardian. Provides a narrow
    interface to the mementos."""

    def __init__(self, originator) -> None:
        self._mementos = []
        self._originator = originator

    def create(self):
        """Store a new Memento of the Originators current state"""
        print("CareTaker: Getting a copy of Originators current state ...")
        memento = self._originator.memento
        self._mementos.append(memento)

    def restore(self, index):
        """Replace the Originators current state
        with the state stored in the saved Memento."""

        print("CareTaker: Restoring Originators state from Memento")
        memento = self._mementos[index]
        self._originator.memento = memento


# ==========================================
#                   tests
# ==========================================
if __name__ == "__main__":

    class TestMementoPattern(TestCase):
        """A Test Class for the Memento pattern"""

        def test_memento(self):
            """A method to test the Memento class"""

            # the client
            originator = Originator()
            caretaker = Caretaker(originator)

            # originators state can change
            # periodically due to application events
            originator.state = "State #1"
            originator.state = "State #2"

            # save the state of the originator
            caretaker.create()

            # add more changes, and then perform another backup
            originator.state = "State #3"
            caretaker.create()

            originator.state = "State #4"
            caretaker.create()

            # restore first state from backup
            caretaker.restore(0)
            self.assertEqual(originator.state, "State #2")

            # restore second state from backup
            caretaker.restore(1)
            self.assertEqual(originator.state, "State #3")


    runner = TextTestRunner()
    runner.run(TestMementoPattern('test_memento'))