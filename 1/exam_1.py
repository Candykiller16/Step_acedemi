# Создайте небольшую программу для сети кофеен. Программа должна вычислять
# стоимость заказанного кофе с учетом возможных добавок (сахара, молока, взбитых
# сливок). Например, эспрессо с сахаром или американо с сахаром, молоком и взбитыми
# сливками.
# В программе обязательно должны быть реализованы следующие классы:
# • класс Coffee – базовый класс для напитка. Должен содержать метод
# getCost(), который будет возвращать стоимость напитка, и метод
# getDescription(), который будет возвращать описание напитка.
# • класс Espresso
# • класс Amerikano
# • класс DarkRoast
# • класс Milk
# • класс Sugar
# • класс Whip
#
# Перегрузите магические методы __str__ и __repr__. Поддержите возможность выводить информацию о заказе в файл.
class Sugar(object):

    @classmethod
    def getName(cls):
        return f"{cls.__name__}"

    def __init__(self, sugar):
        self.sugar = sugar

    def getCostOfSugar(self):
        return self.sugar


class Cofee(object):

    @classmethod
    def getName(cls):
        return f"{cls.__name__}"

    def __init__(self, sugar, cost=0, milk=0, whipped_cream=0):
        self.cost = cost
        self.sugar = sugar

        self.milk = milk
        self.whipped_cream = whipped_cream


    def getCost(self):
        if self.sugar:
            return self.cost + self.sugar.getCostOfSugar()
        else:
            return self.cost
        # if self.sugar or self.milk or self.whipped_cream:
        #     return self.cost + self.sugar.getCostOfSugar() + self.milk + self.whipped_cream
        # else:
        #     return self.cost

    def getDescription(self):
            if self.sugar and self.milk and self.whipped_cream:
                return f'Ваш {Cofee.getName()}, c сахаром, молоком и взбитыми сливками'
            elif self.sugar and self.milk:
                return f'Ваш {Cofee.getName()}, c сахаром, молоком'
            elif self.sugar:
                return f'Ваш {Cofee.getName()}, c сахаром'
            else:
                return f'Ваш {Cofee.getName()}'


sugar = Sugar(2)
b = Cofee(15)
print(b.getCost())
print(b.getDescription())
