from abc import ABC, abstractmethod

# The creator class declares the factory method that must
# return an object of a product class. The creator's subclasses
# usually provide the implementation of this method.
class Dialog(ABC):
    # The creator may also provide some default implementation
    # of the factory method.
    @abstractmethod
    def createButton(self):
        pass

    # Note that, despite its name, the creator's primary
    # responsibility isn't creating products. It usually
    # contains some core business logic that relies on product
    # objects returned by the factory method. Subclasses can
    # indirectly change that business logic by overriding the
    # factory method and returning a different type of product
    # from it.
    def render(self):
        # Call the factory method to create a product object.
        okButton = self.createButton()
        # Now use the product.
        okButton.onClick(self.closeDialog)
        okButton.render()

    def closeDialog(self):
        print("Dialog closed.")


# Concrete creators override the factory method to change the
# resulting product's type.
class WindowsDialog(Dialog):
    def createButton(self):
        return WindowsButton()


class WebDialog(Dialog):
    def createButton(self):
        return HTMLButton()


# The product interface declares the operations that all
# concrete products must implement.
class Button(ABC):
    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def onClick(self, f):
        pass


# Concrete products provide various implementations of the
# product interface.
class WindowsButton(Button):
    def render(self):
        print("Render a button in Windows style.")

    def onClick(self, f):
        print("Bind a native OS click event.")


class HTMLButton(Button):
    def render(self):
        print("Return an HTML representation of a button.")

    def onClick(self, f):
        print("Bind a web browser click event.")


class Application:
    def __init__(self):
        self.dialog = None

    # The application picks a creator's type depending on the
    # current configuration or environment settings.
    def initialize(self):
        config = self.readApplicationConfigFile()

        if config["OS"] == "Windows":
            self.dialog = WindowsDialog()
        elif config["OS"] == "Web":
            self.dialog = WebDialog()
        else:
            raise Exception("Error! Unknown operating system.")

    def readApplicationConfigFile(self):
        # Simulated method to read the application configuration
        # file and return the configuration as a dictionary.
        return {"OS": "Windows"}  # Simulated configuration

    # The client code works with an instance of a concrete
    # creator, albeit through its base interface. As long as
    # the client keeps working with the creator via the base
    # interface, you can pass it any creator's subclass.
    def main(self):
        self.initialize()
        self.dialog.render()


# Usage
app = Application()
app.main()
