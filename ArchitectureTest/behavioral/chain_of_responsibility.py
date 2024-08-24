"""
Description:
------------
Chain of Responsibility pattern is a behavioral pattern used to achieve loose coupling in
software design. In this pattern, an object is passed to a Successor, and depending on some
kind of logic, will or won't be passed onto another successor and processed. This process of
passing objects through multiple successors is called a chain.

Key Features:
------------
- The object that is passed between each successor does not know about which successor will
  handle it. It is an independent object that may or may not be processed by a particular
  successor before being passed onto the next.

- The chain that the object will pass through is normally dynamic at runtime, although you
  can hard code the order or start of the chain, so each successor will need to comply with
  a common interface that allows the object to be received and passed onto the next successor.
"""