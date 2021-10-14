class Person:
    def __init__(self, name, age, surname=''):
        self._name = name
        self._surname = surname
        self._age = age

    def getPersonalData(self):
        print('Я беларус. Мяне клiчуць {} {} па-батьку. Мне {} ад нараджэння Хрыста'.format(
            self._name, self._surname, self._age))


    def getName(self): # геттер
        return self._name

    def getSurname(self):
        return self._surname

    def getAge(self):
        return self._age



# def testClass():
#     p1 = Person('Anton', 2021 , 'Arkhipau')
#     print('Наш первый человек = ', p1.name)
#     p2 = Person('Eva', age=2020)
#     print('Это первая женщина = ', p1.name)
#     p3 = Person('Avel', age=2000)
#     print('Это сын {0} и {1} - {2}'.format(p1.name, p2.name, p3.name))
#     p4 = Person('Vasia', 1950, 'Ivanov')
#     print('А потом появился {} {}'.format(p4.name, p4.surname))
#     p4.name = 'Huiasia'
#     p4.surname = 'Ty'
#     p4.age = 18
#
#     human_world = [p1, p2, p3, p4]
#     for i in human_world:
#        i.getPersonalData()

class Student(Person):
    def __init__(self, name, surname, age, university):
        super(Student, self).__init__(name, age, surname)
        self.__university = university
        self.__marks = {}

    def getUnivetsity(self):
        return self.__university

    def getMarks(self):
        return self.__marks

    def getPersonalData(self):
        super(Student, self).getPersonalData()
        print('Я учусь в {}.'.format(self.__university))


    def getStudentInfo(self):
        print('Я студент {} {}'.format(self._name, self._surname))
        print('Моя успеваемость:', self.__marks)

#
# Если мы хотим использовать атрибуты род класса в дочернем, то делай в род классе их protected, с private не
# сработает.
