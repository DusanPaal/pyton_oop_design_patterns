"""
Description:
------------
The Interpreter pattern is a design pattern used to convert information
from one language into another. This language could be anything from words
in a sentence to numerical formulas or software code. The pattern works
by converting the source information into an Abstract Syntax Tree (AST)
made up of Terminal and Non-Terminal expressions, each implementing an
interpret() method.

Key Features:
-------------
Grammatical Rules Representation:
    The pattern represents each grammatical rule with a class.

Abstract Syntax Tree (AST):
    The AST is composed of Terminal and Non-Terminal expressions.
    Terminal expressions are final (requiring no further processing),
    while Non-Terminal expressions are combinations of Terminal and/or
    other Non-Terminal expressions. The AST starts with a Non-Terminal
    expression and resolves down each branch until all expressions terminate.

Usage:
------
- The Interpreter pattern is typically used when there is a need to interpret
  or evaluate sentences in a particular language, whether that language is natural
  (like English), mathematical, or a programming language.
"""

from unittest import TestCase, TextTestRunner

class AbstractExpression:

    @staticmethod
    def interpret():
        """The `interpret` method gets called
        recursively for each AbstractExpression"""

class Number(AbstractExpression):
    """Terminal Expression"""

    def __init__(self, value):
        self.value = int(value)

    def interpret(self):
        return self.value

    def __repr__(self):
        return str(self.value)

class Add(AbstractExpression):
    """Non-Terminal Expression"""

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() + self.right.interpret()

    def __repr__(self):
        return f"({self.left} Add {self.right})"

class Subtract(AbstractExpression):
    """Non-Terminal Expression"""

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() - self.right.interpret()

    def __repr__(self):
        return f"({self.left} Subtract {self.right})"


# ==========================================
#                   tests
# ==========================================
if __name__ == "__main__":

    class TestInterpreterPattern(TestCase):
        """A Test Class for the Interpreter pattern"""

        def test_interpreter(self):
            """A method to test the Interpreter class"""

            sentence = "5 + 4 - 3 + 7 - 2"

            print(sentence)
            # Split the sentence into individual expressions that will be added to
            # an Abstract Syntax Tree (AST) as Terminal and Non-Terminal expressions
            tokens = sentence.split(" ")
            print(tokens)

            # Manually Creating an Abstract Syntax Tree from the tokens
            ast: list[AbstractExpression] = []                      # A list of AbstractExpressions
            ast.append(Add(Number(tokens[0]), Number(tokens[2])))   # 5 + 4
            ast.append(Subtract(ast[0], Number(tokens[4])))         # ^ - 3
            ast.append(Add(ast[1], Number(tokens[6])))              # ^ + 7
            ast.append(Subtract(ast[2], Number(tokens[8])))         # ^ - 2

            # Use the final AST row as the root node.
            ast_root = ast.pop()

            # Interpret recursively through the full AST starting from the root.
            print(ast_root.interpret())

            # Print out a representation of the AST_ROOT
            print(ast_root)

    runner = TextTestRunner()
    runner.run(TestInterpreterPattern('test_interpreter'))