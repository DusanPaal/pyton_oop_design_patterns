# Description.
# ------------
# The Composite design pattern is a structural pattern useful for hierarchal management.
# It allows you to compose objects into tree structures to represent part-whole hierarchies.
# The pattern lets clients treat individual objects and compositions of objects uniformly.

# Useful when:
# ------------
# - You want to represent part-whole hierarchies of objects (e.g. file systems)
# - Any system where you need to offer at runtime the ability to group, un-group, modify multiple
# objects at the same time, would benefit from the composite design pattern structure. Programs
# that allow you to draw shapes and graphics will often also use this structure as well
# - File explorer on windows is a very good example of the composite design pattern in use
#
# Key features:
# ------------
# - It provides flexibility of structure since you can add/remove and reorder components

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

        parent_id = None

        if self.reference_to_parent:
            parent_id = id(self.reference_to_parent)

        print(
            f"<Leaf>\t\tid:{id(self)}\tParent:\t{parent_id}"
        )

    @staticmethod
    @abstractmethod
    def detach(self):
        "Detaching this leaf from its parent composite"

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
        """The method handle""")

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