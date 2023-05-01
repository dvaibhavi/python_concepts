# Example of implementing the Singleton Design Pattern in Python

class Singleton:
    __instance = None

    def __init__(self):
        if Singleton.__instance is not None:
            raise Exception("This class is a Singleton!")
        else:
            Singleton.__instance = self

    @staticmethod
    def get_instance():
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance

s1 = Singleton.get_instance()
s2 = Singleton.get_instance()

print(s1 is s2) # Output: True

'''
When implementing a singleton in Python, it's important to consider thread-safety 
and serializability to ensure that the singleton object is always consistent and 
can be safely accessed from multiple threads or processes. Here are two approaches to 
implement a thread-safe and serializable singleton in Python:

1. Using a metaclass
A metaclass is a class that defines the behavior of other classes. 
By using a metaclass, you can ensure that only one instance of a class is created and 
that it is thread-safe.
'''
import threading

class SingletonMeta(type):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]

class MyClass(metaclass=SingletonMeta):
    pass

'''

In this example, we define a SingletonMeta metaclass that keeps track of the 
instances of the classes that use it. We use a lock to ensure that the instance creation 
is thread-safe. The __call__ method of the metaclass is called whenever an instance of a class 
that uses the metaclass is created. It checks whether an instance of the class already exists and,
 if not, creates a new instance and stores it in the _instances dictionary.


2. Using a decorator
A decorator is a function that takes a function or a class and returns a new function or
 class with additional behavior. By using a decorator, you can wrap a class in a function that 
 ensures that only one instance of the class is created and that it is thread-safe.
'''

import threading

def singleton(cls):
    _instances = {}
    _lock = threading.Lock()

    def get_instance(*args, **kwargs):
        with _lock:
            if cls not in _instances:
                instance = cls(*args, **kwargs)
                _instances[cls] = instance
        return _instances[cls]

    return get_instance

@singleton
class MyClass:
    pass
