def printRules():
    print('НЕ курите! Не распивайте спиртные напитки.')
    print('Носите маски! И будте здоровы!')

class Carriage:
    def __init__(self, numberOfSeats, carriageType, number):
        self.__numberOfSeats = numberOfSeats
        self.__carriageType = carriageType
        self.__number = number
        self.__seats = [0] * numberOfSeats
        # self.__seats = [False for i in range(self.__numberOfSeats)]

    @property
    def seats(self):
        return self.__seats

    @property
    def numberOfSeats(self):
    # def getNumberOfSeats(self):
        return self.__numberOfSeats

    @property
    def carriageType(self):
    # def getCarriageType(self):
        return self.__carriageType

    @property
    def number(self):
    # def getNumber(self):
        return self.__number

    def getShortInfo(self):
        return str(self.__number) + self.__carriageType

    def hasFreeSeats(self):
        return False in self.__seats

    def buySeat(self, seatNumber):
        if 0 < seatNumber <= self.__numberOfSeats:
            number = seatNumber-1
            if self.__seats[number] == 0:
                self.__seats[number] = 1
                return True
        return False

    def getFreeSeats(self):
        res = []
        for index, isNotFree in enumerate(self.__seats):
            if not isNotFree:
                res.append(index+1)
        return res

    def getFreeSeatsCount(self):
        return self.__seats.count(0)


    def getBusySeatsCount(self):
        print('Издевательство')
        self.getRules() # self знает о staticmethod, но staticmethod не знает о self,
        # поэтому его можно исп внутри методов
        return self.__seats.count(1)

    def free_Jango(self, seatNumber):
        if 0 < seatNumber <= self.__numberOfSeats:
            number = seatNumber-1 # ищем индекс
            if self.__seats[number] == 1:
                self.__seats[number] = 0
                return True
        return False

    @staticmethod
    def getRules():
        print('НЕ курите! Не распивайте спиртные напитки.')
        print('Носите маски! И будте здоровы!')

    # Статический метод связан только логичски с нашим классом








# one = Carriage(20, 'СВ', 5)
# getNumberOfSeats = one.getNumberOfSeats()
# getCarriageType = one.getCarriageType()
# getNumber = one.getNumber()
# print(getNumber, getCarriageType, getNumberOfSeats)
# one.__getattribute__('numberOfSeats')