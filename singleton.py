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
