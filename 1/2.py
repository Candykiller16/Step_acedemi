class Sugar(object):

    def __init__(self):
        self.sugar = 0

    def getCostOfSugar(self):
        self.sugar = int(input("Enter 0, if you don't want sugar, or 2 if you want add sugar: "))
        return self.sugar


class Milk(object):

    def __init__(self):
        self.milk = 0

    def getCostOfMilk(self):
        self.milk = int(input("Enter 0, if you don't want milk, or 4 if you want add milk: "))
        return self.milk


class Whip(object):

    def __init__(self):
        self.whip = 0

    def getCostOfWhip(self):
        self.whip = int(input("Enter 0, if you don't want to add whip, or 6 if you want to add whip: "))
        return self.whip


class Cofee(object):

    def __init__(self, cost, sugar, milk, whip):
        self.cost = cost
        self.obj_sugar = sugar
        self.obj_milk = milk
        self.obj_whip = whip


    @classmethod
    def getName(cls):
        return f"{cls.__name__}"


    def getCost(self):
        s = self.obj_sugar.getCostOfSugar()  # add sugar
        m = self.obj_milk.getCostOfMilk()  # add milk
        w = self.obj_whip.getCostOfWhip()  # add whip

        if s == 0 and m == 0 and w == 0:  # without adds
            return f'The price of your {Cofee.getName()} is {self.cost}'
        elif s and m == 0 and w == 0:  # with sugar
            return f'The price of your {Cofee.getName()} with sugar is {self.cost + s}'
        elif s and m and w == 0:  # with sugar and milk
            return f'The price of your {Cofee.getName()} with sugar and milk is {self.cost + s + m}'
        elif s and m == 0 and w:  # with sugar and whip
            return f'The price of your {Cofee.getName()} with sugar and whip is {self.cost + s + w}'
        elif s == 0 and m and w == 0:  # with milk
            return f'The price of your {Cofee.getName()} with milk is {self.cost + m}'
        elif s == 0 and m and w:  # with milk and whip
            return f'The price of your {Cofee.getName()} with milk amd whip is {self.cost + m + w}'
        elif s == 0 and m == 0 and w:  # with whip
            return f'The price of your {Cofee.getName()} with whip is {self.cost + w}'
        elif s and m and w:  # with everything
            return f'The price of your {Cofee.getName()} with sugar, milk amd whip is {self.cost + s + m + w}'


    def getDiscription(self):
        # s = self.obj_sugar.getCostOfSugar()  # add sugar
        # m = self.obj_milk.getCostOfMilk()  # add milk  HOW TO SAVE RESULT OF THIS AND USE IT IN THIS METHOD ?
        # w = self.obj_whip.getCostOfWhip()  # add whip

        self.getCost()
        if s == 0 and m == 0 and w == 0:  # without adds
            return f'Your {Cofee.getName()}'
        elif s and m == 0 and w == 0:  # with sugar
            return f'Your {Cofee.getName()} with sugar'
        elif s and m and w == 0:  # with sugar and milk
            return f'Your {Cofee.getName()} with sugar and milk'
        elif s and m == 0 and w:  # with sugar and whip
            return f'Your {Cofee.getName()} with sugar and whip'
        elif s == 0 and m and w == 0:  # with milk
            return f'Your {Cofee.getName()} with milk'
        elif s == 0 and m and w:  # with milk and whip
            return f'Your {Cofee.getName()} with milk amd whip'
        elif s == 0 and m == 0 and w:  # with whip
            return f'Your {Cofee.getName()} with whip'
        elif s and m and w:  # with everything
            return f'Your {Cofee.getName()} with sugar, milk amd whip '


class Espresso(Cofee):
    def getCost(self):
        s = self.obj_sugar.getCostOfSugar()  # add sugar
        m = self.obj_milk.getCostOfMilk()  # add milk
        w = self.obj_whip.getCostOfWhip()  # add whip

        if s == 0 and m == 0 and w == 0:  # without adds
            return f'The price of your {Espresso.getName()} is {self.cost}'
        elif s and m == 0 and w == 0:  # with sugar
            return f'The price of your {Espresso.getName()} with sugar is {self.cost + s}'
        elif s and m and w == 0:  # with sugar and milk
            return f'The price of your {Espresso.getName()} with sugar and milk is {self.cost + s + m}'
        elif s and m == 0 and w:  # with sugar and whip
            return f'The price of your {Espresso.getName()} with sugar and whip is {self.cost + s + w}'
        elif s == 0 and m and w == 0:  # with milk
            return f'The price of your {Espresso.getName()} with milk is {self.cost + m}'
        elif s == 0 and m and w:  # with milk and whip
            return f'The price of your {Espresso.getName()} with milk amd whip is {self.cost + m + w}'
        elif s == 0 and m == 0 and w:  # with whip
            return f'The price of your {Espresso.getName()} with whip is {self.cost + w}'
        elif s and m and w:  # with everything
            return f'The price of your {Espresso.getName()} with sugar, milk amd whip is {self.cost + s + m + w}'


class Americano(Cofee):
    def getCost(self):
        s = self.obj_sugar.getCostOfSugar()  # add sugar
        m = self.obj_milk.getCostOfMilk()  # add milk
        w = self.obj_whip.getCostOfWhip()  # add whip

        if s == 0 and m == 0 and w == 0:  # without adds
            return f'The price of your {Americano.getName()} is {self.cost}'
        elif s and m == 0 and w == 0:  # with sugar
            return f'The price of your {Americano.getName()} with sugar is {self.cost + s}'
        elif s and m and w == 0:  # with sugar and milk
            return f'The price of your {Americano.getName()} with sugar and milk is {self.cost + s + m}'
        elif s and m == 0 and w:  # with sugar and whip
            return f'The price of your {Americano.getName()} with sugar and whip is {self.cost + s + w}'
        elif s == 0 and m and w == 0:  # with milk
            return f'The price of your {Americano.getName()} with milk is {self.cost + m}'
        elif s == 0 and m and w:  # with milk and whip
            return f'The price of your {Americano.getName()} with milk amd whip is {self.cost + m + w}'
        elif s == 0 and m == 0 and w:  # with whip
            return f'The price of your {Americano.getName()} with whip is {self.cost + w}'
        elif s and m and w:  # with everything
            return f'The price of your {Americano.getName()} with sugar, milk amd whip is {self.cost + s + m + w}'

class DarkRoast(Cofee):
    def getCost(self):
        s = self.obj_sugar.getCostOfSugar()  # add sugar
        m = self.obj_milk.getCostOfMilk()  # add milk
        w = self.obj_whip.getCostOfWhip()  # add whip

        if s == 0 and m == 0 and w == 0:  # without adds
            return f'The price of your {DarkRoast.getName()} is {self.cost}'
        elif s and m == 0 and w == 0:  # with sugar
            return f'The price of your {DarkRoast.getName()} with sugar is {self.cost + s}'
        elif s and m and w == 0:  # with sugar and milk
            return f'The price of your {DarkRoast.getName()} with sugar and milk is {self.cost + s + m}'
        elif s and m == 0 and w:  # with sugar and whip
            return f'The price of your {DarkRoast.getName()} with sugar and whip is {self.cost + s + w}'
        elif s == 0 and m and w == 0:  # with milk
            return f'The price of your {DarkRoast.getName()} with milk is {self.cost + m}'
        elif s == 0 and m and w:  # with milk and whip
            return f'The price of your {DarkRoast.getName()} with milk amd whip is {self.cost + m + w}'
        elif s == 0 and m == 0 and w:  # with whip
            return f'The price of your {DarkRoast.getName()} with whip is {self.cost + w}'
        elif s and m and w:  # with everything
            return f'The price of your {DarkRoast.getName()} with sugar, milk amd whip is {self.cost + s + m + w}'

sugar = Sugar()
milk = Milk()
whip = Whip()
cofee = Cofee(15, sugar, milk, whip)
# print(cofee.getCost())
espresso = Espresso(15, sugar, milk, whip)
americano = Americano(15, sugar, milk, whip)
dark_roast = DarkRoast(15, sugar, milk, whip)
print(americano.getCost())
