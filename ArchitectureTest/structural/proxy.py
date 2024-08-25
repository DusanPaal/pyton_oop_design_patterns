"""
Description:
------------
The Proxy Pattern is a structural design pattern that provides an interface to
another class or object, acting as a stand-in or surrogate. The proxy controls
access to the real subject, allowing for additional functionality such as caching,
authentication, or lazy initialization.

Types of Proxies:

1. Virtual Proxy:
    Delays the creation or loading of an expensive object until it is needed.
    It can also cache parts of the real object, completing the loading as required.

2. Remote Proxy:
    Manages communication between a client and a remote object in a different
    address space, often in a different machine or server.

3. Protection Proxy:
    Controls access to the real object by adding an authentication or
    authorization layer before granting access.

4. Smart Reference:
    Provides additional functionality when accessing an object, such as counting
    the number of references, loading, or handling additional responsibilities.

Key Features:
-------------
Enhanced Functionality:
    Proxies can add functionalities like caching, validation, logging, lazy
    initialization, or access control before forwarding requests to the real
    object.

Interface Matching:
    The proxy should closely match the subject's interface so that it appears
    identical to the client, making the substitution seamless.

Versatility:
    Proxies can handle a variety of tasks, depending on the type of proxy used,
    making them versatile in different scenarios.

Monkey Patching/Object Augmentation:
    The proxy pattern can be seen as a form of monkey patching or object
    augmentation, where the behavior of an object is modified or extended
    at runtime.

Request Forwarding:
    The proxy forwards requests to the real subject based on its type, managing
    how and when the real subject is accessed.

Authentication and Access Control:
    A protection proxy, similar to an NGINX proxy, can enforce authentication
    mechanisms, such as Basic Authentication, to control access.

Proxy vs. Adapter vs. Decorator:
    Unlike an Adapter, which adapts two incompatible interfaces, a Proxy uses
    the same interface as the subject. Similar to a Facade, but with the ability
    to add responsibilities like a Decorator, which can be used recursively.

Convenient Stand-in:
    The Proxy provides a stand-in when direct access to the real subject is
    inconvenient, costly, or requires additional control.

Surrogate Pattern:
    The Proxy pattern is also known as the Surrogate design pattern, emphasizing
    its role as a substitute for another object.

Usage:
------
- You need to control access to an object, adding an extra layer of functionality
    such as caching, logging, or access control.

- The object is resource-intensive to create or requires expensive operations,
    and you want to delay its creation until absolutely necessary.

- The object is in a different address space, such as on a remote server, and
    you need to manage communication between the client and the remote object.

- You want to add a security layer that ensures only authorized clients can
    access the real object.
"""

from abc import ABCMeta, abstractmethod
from unittest import TestCase, TextTestRunner


class ISubject(metaclass=ABCMeta):
    """An interface implemented by both the Proxy and Real Subject"""

    @staticmethod
    @abstractmethod
    def request(self):
        """A method to implement"""


class RealSubject(ISubject):
    """The actual real object
    that the proxy is representingt"""

    def __init__(self):
        """Constructs the real object"""

        # hypothetically enormous amounts of data
        self.enormous_data = [1, 2, 3]

    def request(self):
        """The real request"""
        return self.enormous_data


class Proxy(ISubject):
    """The virtual proxy. In this case the proxy will act as a cache for
    `enormous_data` and only populate the enormous_data when it
    is actually necessary"""

    def __init__(self):
        """Constructs the proxy"""

        self.enormous_data = []
        self.real_subject = RealSubject()

    def request(self):
        """Using the proxy as a cache,
        and loading data into it only
        if it is needed"""

        if self.enormous_data == []:
            print("Pulling data from RealSubject")
            self.enormous_data = self.real_subject.request()
            return self.enormous_data

        print("Pulling data from Proxy cache...")
        return self.enormous_data


# ==========================================
#                   tests
# ==========================================
if __name__ == "__main__":

    class TestProxyPattern(TestCase):
        """A Test Class for the Flyweight Pattern"""

        def test_proxy_pattern(self):
            """A test method to test the proxy pattern"""

            # The Client
            proxy = Proxy()

            # use proxy
            print(id(proxy))

            # load the enormous amounts of data
            # because now we want to show it.
            data = proxy.request()
            self.assertEqual(data, [1, 2, 3])

            # show the data again, but this time
            # it retrieves it from the local cache
            data = proxy.request()
            self.assertEqual(data, [1, 2, 3])

    runner = TextTestRunner()
    runner.run(TestProxyPattern('test_proxy_pattern'))