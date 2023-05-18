'''
Note that the readApplicationConfigFile() function is not defined in the given code snippet. 
You would need to implement it separately to read the application configuration from a file or from any other source.

source :- https://refactoring.guru/design-patterns/abstract-factory 
'''

from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def paint(self):
        pass


class WinButton(Button):
    def paint(self):
        print("Render a button in Windows style.")


class MacButton(Button):
    def paint(self):
        print("Render a button in macOS style.")


class Checkbox(ABC):
    @abstractmethod
    def paint(self):
        pass


class WinCheckbox(Checkbox):
    def paint(self):
        print("Render a checkbox in Windows style.")


class MacCheckbox(Checkbox):
    def paint(self):
        print("Render a checkbox in macOS style.")


class Application:
    def __init__(self, factory):
        self.factory = factory
        self.button = None

    def createUI(self):
        self.button = self.factory.createButton()

    def paint(self):
        self.button.paint()


class ApplicationConfigurator:
    def main(self):
        config = readApplicationConfigFile()

        if config.OS == "Windows":
            factory = WinFactory()
        elif config.OS == "Mac":
            factory = MacFactory()
        else:
            raise Exception("Error! Unknown operating system.")

        app = Application(factory)
        app.createUI()
        app.paint()
