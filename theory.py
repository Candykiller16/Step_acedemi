# Объектно-ориентированное программирование
#
# Класс содержит поля(данные(properties)) и методы(функции(methods))
#
# Может быть создано много экземпляров(объектов) одного класса
#
# Три принципа ООП "три кита"

# Инкапсуляция:
# * сокрытие в классе данных, чтобы они не были доступны снаружи
# * оъединение данных и методов, с помощью которых эти данные обрабатываются

# "Принцип открытости и закрытости" - что я могу предоставить другим пользователям

# Наследование:
# Выстраивание иерархии с род и доч классами
# Есть родительский класс, и дочерние классы, которые могу наследовать свойства и методы родительского класса.
# Производные классы получают "по наследству" данные и методы своих базовых классов и расширять

# Полиморфизм:
# 1) Способность вести себя по разному в зависимости от ситуации
# 2) Способность объекта использовать методы производного класса (меняем функциаонал класса в род классах,
# но имеем одинаковое название)

class MyFirstClass(object):
    def __init__(self, value):
        self.__myValue = value

    def getValue(self):
        return self.__myValue

    def updateValue(self, value):
        if value > 0:
            self.__myValue = value

object1 = MyFirstClass(42)
object1.getValue()

object2 = MyFirstClass()
object2.getValue()

# Модификаторы доступа:
#
# public - поля и методы доступны везде
#
# protected - в собственных методах класса, в произодных классах
#
# private - в собственных методах класса