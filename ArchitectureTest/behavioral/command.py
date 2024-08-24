"""
Description:
------------
The Command pattern is a behavioral design pattern that separates
the object invoking a command from the object performing it.
For example, a button (Invoker) triggers a command that is executed
by a Receiver, which then calls a pre-registered Command object.

Benefits:
---------
This pattern allows for separation of concerns, enabling independent
problem-solving, such as logging command execution and outcomes.

Useful When:
------------
- Implementing UNDO/REDO functionality.
- Handling GUI Buttons, menus, macro recording, multi-level undo/redo,
networking (e.g., sending command objects across a network), batch
processing, parallel processing, thread pools, transactional behavior,
and wizards.

Key Features:
------------
The Command object should not manage state.
One or more Invokers can execute the Command later.
Similar to the Memento pattern for UNDO/REDO purposes, but while Memento
records and restores object states, the Command pattern executes predefined
commands like Draw, Turn, Resize, or Save.
"""

from abc import ABCMeta, abstractmethod
from unittest import TestCase, TextTestRunner


class ICommand (metaclass=ABCMeta):
    """The command interface, that
    all commands will implement"""

    @staticmethod
    @abstractmethod
    def execute(self):
        """The required execute method
        that all command objects will use"""

class Command1(ICommand):
    """A Command object, that implements the ICommand
    interface and runs the command on the designated receiver"""

    def __init__(self, receiver):
        """Constructs the Command1 object"""
        self._receiver = receiver

    def execute(self):
        self._receiver.run_command_1()

class Command2(ICommand):
    """A Command object, that implements the ICommand
    interface and runs the command on the designated receiver"""

    def __init__(self, receiver):
        """Constructs the Command2 object"""
        self._receiver = receiver

    def execute(self):
        self._receiver.run_command_2()

class Receiver:
    """The Receiver"""

    @staticmethod
    def run_command_1():
        "A set of instructions to run"
        print("Executing Command 1")

    @staticmethod
    def run_command_2():
        "A set of instructions to run"
        print("Executing Command 2")

class Invoker:
    """The Invoker Class"""

    def __init__(self):
        """Constructs the Invoker"""
        self._commands = {}

    def register(self, command_name, command):
        """Register commands in the Invoker"""
        self._commands[command_name] = command

    def execute_commands(self, command_name):
        """Execute any registered commands"""

        if command_name in self._commands.keys():
            self._commands[command_name].execute()
        else:
            print(f"Command [{command_name}] not recognised")


# ==========================================
#                   tests
# ==========================================
if __name__ == "__main__":

    class TestCommandPattern(TestCase):
        """A Test Class for the Command Pattern"""

        def test_command(self):
            """A method to test the Command class"""

            # The CLient
            # Create a receiver
            receiver = Receiver()

            # Create Commands
            command_1 = Command1(receiver)
            command_2 = Command2(receiver)

            # Register the commands with the invoker
            invoker = Invoker()
            invoker.register("1", command_1)
            invoker.register("2", command_2)

            # Execute the commands that are registered on the Invoker
            invoker.execute_commands("1") # should print "Executing Command 1"
            invoker.execute_commands("2") # should print "Executing Command 2"

    runner = TextTestRunner()
    runner.run(TestCommandPattern('test_command'))