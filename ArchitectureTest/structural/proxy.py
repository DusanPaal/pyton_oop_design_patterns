# Description:
# ------------
# The Proxy design pattern provides an interface to another class or object.
#
# Types of Proxies:
# -----------------
# -> Virtual Proxy: Caches parts of the real object and completes loading as needed.
# -> Remote Proxy: Relays messages to a real object in a different address space.
# -> Protection Proxy: Adds an authentication layer before accessing the real object.
# -> Smart Reference: Allows internal attributes of an object to be overridden or replaced.
#
# Key Features:
# -------------
# - Enables additional functionality at the proxy level, such as caching, authorization,
#   validation, lazy initialization, or logging.
# - The proxy should closely match the subject interface to appear identical to the client.
# - Proxy patterns can be referred to as Monkey Patching or Object Augmentation.
# - Forwards requests to the Real Subject based on the proxy type.
# - A protection proxy, like an NGINX proxy, can enforce authentication (e.g., Basic Authentication).
# - Proxies can handle multiple tasks as needed.
# - Unlike an Adapter, which adapts two interfaces, a Proxy uses the same interface as the subject.
# - Similar to a Facade, but with the ability to add responsibilities like a Decorator, which can
#   be used recursively.
# - The Proxy provides a stand-in when direct access to the real subject is inconvenient.
# - The Proxy pattern is also known as the Surrogate design pattern.

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