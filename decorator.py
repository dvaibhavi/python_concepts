# Example of implementing the Decorator Design Pattern in Python

class Pizza:
    def __init__(self):
        self.description = "Plain pizza"

    def get_cost(self):
        return 10

    def get_description(self):
        return self.description

class ToppingDecorator(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza

    def get_cost(self):
        return self.pizza.get_cost()

    def get_description(self):
        return self.pizza.get_description()

class Pepperoni(ToppingDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Pepperoni"

    def get_cost(self):
        return self.pizza.get_cost() + 2

class Mushroom(ToppingDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Mushroom"

    def get_cost(self):
        return self.pizza.get_cost() + 1

pizza = Pizza()
pizza = Pepperoni(pizza)
pizza = Mushroom(pizza)

print(pizza.get_description()) # Output: Plain pizza, Pepperoni, Mushroom
print(pizza.get_cost()) # Output: 13
