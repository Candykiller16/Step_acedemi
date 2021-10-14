from october_14.october_12 import Person, Student

def testClass():
    p1 = Person('Anton', 2021 , 'Arkhipau')
    print('Наш первый человек = ', p1.getName())
    p2 = Person('Eva', age=2020)
    print('Это первая женщина = ', p1.getName())
    p3 = Person('Avel', age=2000)
    print('Это сын {0} и {1} - {2}'.format(p1.getName(), p2.getName(), p3.getName()))
    p4 = Person('Vasia', 1950, 'Ivanov')
    print('А потом появился {} {}'.format(p4.getName(), p4.getSurname()))
    p4.name = 'Huiasia'
    p4.surname = 'Ty'
    p4.age = 18

    human_world = [p1, p2, p3, p4]
    for i in human_world:
       i.getPersonalData()


def testStudent():
    st1 = Student('Bob', 'Rock', 20, 'BSU')
    st1.getPersonalData()
    st1.getStudentInfo()



testStudent()
