class Duck:

    def __init__(self, color, age):
        print('Утка родилась')
        self.color = color
        self.age = age

    def __str__(self):
        return f"I'm a {self.getName()}. My color is {self.color}.My age is {self.age}"


    def delete(self):
        del self
        print('Утки не стало')

    def __eq__(self, other):
        if isinstance(other, Duck):
            return self.age == other.age
        else:
            return f"Нельзя сравнивать {other} с классом {self.getName()}"




    @classmethod
    def getName(cls):
        return f"{cls.__name__}"


    def quack(self):
        raise NotImplementedError

    def swim(self):
        raise NotImplementedError

    def fly(self):
        raise NotImplementedError

class Toy:
    def __init__(self, price='', origin=''):
        print('Игрушка создалась')
        self.price = price
        self.origin = origin

class WildDuck(Duck):

    def quack(self):
        print(f"I'm a {WildDuck.getName()} and I can quack.")

    def swim(self):
        print(f"I'm a {WildDuck.getName()} and I can swim.")

    def fly(self):
        print(f"I'm a {WildDuck.getName()} and I can fly.")

class RedHeadDuck(Duck):

    def quack(self):
        print(f"I'm a {RedHeadDuck.getName()} and I can quack.")

    def swim(self):
        print(f"I'm a {RedHeadDuck.getName()} and I can swim.")

    def fly(self):
        print(f"I'm a {RedHeadDuck.getName()} and I can fly.")

class DecoyDuck(Duck):

    def swim(self):
        print(f"I'm a {DecoyDuck.getName()} and I can swim.")


class RubberDuck(Duck):

    def quack(self):
        print(f"I'm a {RubberDuck.getName()} and I can quack.")

    def swim(self):
        print(f"I'm a {RubberDuck.getName()} and I can swim.")

class ToyDuck(Duck, Toy):

    def __init__(self, color, age, price, origin): # как унаследовать поля класса Toy ?
        Duck.__init__(self, color, age)
        Toy.__init__(self, price, origin)


    def __str__(self):
        return f"I'm a {self.getName()}. My color is {self.color}.My age is {self.age}. My price is {self.price}." \
               f"My origin is {self.origin}"

    def quack(self):
        print(f"I'm a {ToyDuck.getName()} and I can quack.")


c = ToyDuck('red', 18, 500, 'Viatnam') # Утка родилась
print(c)
# d = ToyDuck('blue', 18, 500, 'Viatnam') # Утка родилась
# print(c)
# print(c == d) # True
# print(c == 18) # Нельзя сравнивать 18 с классом ToyDuck

#print(c) # name 'c' is not defined
