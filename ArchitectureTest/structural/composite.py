"""
Description:
------------
The Composite Pattern is a structural design pattern that allows you to compose
objects into tree-like structures to represent part-whole hierarchies. This
pattern enables clients to treat individual objects and compositions of objects
in a uniform manner.

Key features:
-------------
Uniform Treatment:
    The pattern allows clients to treat individual objects and compositions
    (groups of objects) in the same way. This simplifies code that interacts
    with these objects, as it doesn't need to differentiate between single
    and composite objects.

Flexible Structure:
    The Composite Pattern provides flexibility in managing the structure,
    as components can be added, removed, or reordered dynamically. This is
    useful in systems where the composition of objects may change over time.

Recursive Composition:
    Objects in the composite structure can themselves be composites, allowing
    for complex hierarchies. For instance, a folder can contain both files and
    other folders, which can themselves contain files and folders.

Usage:
------
Part-Whole Hierarchies:
    When you need to represent a hierarchy of objects where individual objects
    and compositions of objects should be treated uniformly.

Grouping and Management:
    When your system requires the ability to group, ungroup, or modify multiple
    objects simultaneously at runtime, the Composite Pattern is beneficial.
    This is common in applications like graphic editors or file systems.

File Systems:
    A classic example is a file system where files and folders (directories)
    are organized in a hierarchical structure. The Composite Pattern allows
    treating files and folders uniformly when performing operations like opening,
    closing, or displaying their contents.

"""

from abc import ABCMeta, abstractmethod


class IComponent(metaclass=ABCMeta):
    """A component interface describing the common
    fields and methods of leaves and composites"""

    reference_to_parent = None

    @staticmethod
    @abstractmethod
    def method():
       """"A method each Leaf
       and composite container
       should implement"""

    @staticmethod
    @abstractmethod
    def detach(child):
        """Called before a leaf
        is attached to a composite"""


class Leaf(IComponent):
    """A Leaf can be added to
    a composite, but not a leaf"""

    reference_to_parent = None

    @staticmethod
    @abstractmethod
    def method(self):
        """The method handle"""

        parent_id = None

        if self.reference_to_parent:
            parent_id = id(self.reference_to_parent)

        print(f"<Leaf>\t\tid:{id(self)}\tParent:\t{parent_id}")

    @staticmethod
    @abstractmethod
    def detach(self):
        """Detaching this leaf from its parent composite"""

        if self.reference_to_parent is not None:
            self.reference_to_parent.delete(self)


class Composite(IComponent):
    """A composite can contain leaves and compositess"""

    def  __init__(self):
        self.components = []

    def method(self):
        """The method handle"""

        parent_id = None

        if self.reference_to_parent:
            parent_id = id(self.reference_to_parent)

        print(
            f"<Composite>\tid:{id(self)}\tParent:\t{parent_id}\t"
            f"Components:{len(self.components)}"
        )

        for component in self.components:
            component.method()

    def reference_to_parent(*args):
        """The method handle"""

    def attach(self, component):
        """Detach leaf/composite from any current parent reference and
        then set the parent reference to this composite (self)"""

        component.detach();
        component.reference_to_parent = self
        self.components.append(component)

    def detach(self):
        """Detaching this composite from its parent composite"""

        if self.reference_to_parent is not None:
            self.reference_to_parent.delete(self)
            self.reference_to_parent = None

    def delete(self, component):
        """"Removes leaf/composite from this composite self.components"""
        self.components.remove(component)