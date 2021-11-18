#Used composition in this task

class Sugar():
    def __init__(self):
        self.sugar = 0

    def getCostOfSugar(self):
        self.sugar = int(input("Enter 0, if you don't want sugar, or 2 if you want add sugar: "))
        return self.sugar

class Milk():
    def __init__(self):
        self.milk = 0

    def getCostOfMilk(self):
        self.milk = int(input("Enter 0, if you don't want milk, or 4 if you want add milk: "))
        return self.milk

class Whip():
    def __init__(self):
        self.whip = 0

    def getCostOfWhip(self):
        self.whip = int(input("Enter 0, if you don't want to add whip, or 6 if you want to add whip: "))
        return self.whip


class Cofee():

    def get_var_name(self):
        for k, v in globals().items():
            if v is self:
                return k

    def __str__(self):
        return f'{self.getDiscriprion()}'

    def __repr__(self):
        return f'{self.getDiscriprion()}'

    def __init__(self):
        self.cost = 0
        self.obj_sugar = Sugar()
        self.obj_milk = Milk()
        self.obj_whip = Whip()

    def setCostofCofee(self):
        self.cost = int(input("Enter cost of coffee: "))

    def getCost(self):
        self.setCostofCofee()
        self.sugar = self.obj_sugar.getCostOfSugar()
        self.milk = self.obj_milk.getCostOfMilk()
        self.whip = self.obj_whip.getCostOfWhip()
        s = self.sugar  # add sugar
        m = self.milk  # add milk
        w = self.whip  # add whip
        if s == 0 and m == 0 and w == 0:  # without adds
            return f'The price of your {self.get_var_name()} is {self.cost}'
        elif s and m == 0 and w == 0:  # with sugar
            return f'The price of your {self.get_var_name()} with sugar is {self.cost + s}'
        elif s and m and w == 0:  # with sugar and milk
            return f'The price of your {self.get_var_name()} with sugar and milk is {self.cost + s + m}'
        elif s and m == 0 and w:  # with sugar and whip
            return f'The price of your {self.get_var_name()} with sugar and whip is {self.cost + s + w}'
        elif s == 0 and m and w == 0:  # with milk
            return f'The price of your {self.get_var_name()} with milk is {self.cost + m}'
        elif s == 0 and m and w:  # with milk and whip
            return f'The price of your {self.get_var_name()} with milk amd whip is {self.cost + m + w}'
        elif s == 0 and m == 0 and w:  # with whip
            return f'The price of your {self.get_var_name()} with whip is {self.cost + w}'
        elif s and m and w:  # with everything
            return f'The price of your {self.get_var_name()} with sugar, milk amd whip is {self.cost + s + m + w}'

    def getDiscriprion(self):
        s = self.sugar  # add sugar
        m = self.milk  # add milk
        w = self.whip  # add whip
        if s == 0 and m == 0 and w == 0:  # without adds
            return f'Your {self.get_var_name()}'
        elif s and m == 0 and w == 0:  # with sugar
            return f'Your {self.get_var_name()} with sugar'
        elif s and m and w == 0:  # with sugar and milk
            return f'Your {self.get_var_name()} with sugar and milk'
        elif s and m == 0 and w:  # with sugar and whip
            return f'Your {self.get_var_name()} with sugar and whip'
        elif s == 0 and m and w == 0:  # with milk
            return f'Your {self.get_var_name()} with milk'
        elif s == 0 and m and w:  # with milk and whip
            return f'Your {self.get_var_name()} with milk and whip '
        elif s == 0 and m == 0 and w:  # with whip
            return f'Your {self.get_var_name()} with whip '
        elif s and m and w:  # with everything
            return f'Your {self.get_var_name()} with sugar, milk and whip'

    def writeDescription(self):
        with open('cofee.txt', 'a') as p:
            p.write(f'{self.getDiscriprion()} \n')

class Americano(Cofee):
    pass

class Espresso(Cofee):
    pass

class DarkRoast(Cofee):
    pass


cofee = Cofee()
americano = Americano()
# print(americano.getCost())
# print(americano.getDiscriprion())

espresso = Espresso()
# print(espresso.getCost())
# print(espresso.getDiscriprion())

darkroast = DarkRoast()
# print(darkroast.getCost())
# print(darkroast.getDiscriprion())

# print(americano)
# print(espresso)
# print(darkroast)


