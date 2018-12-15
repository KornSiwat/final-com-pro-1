import datetime
class Person:
    def __init__(self, name):
        """Create a person"""
        name = name.split(' ')
        self.__name = name[0]
        if len(name) == 3:
            self.__midname = name[1]
            self.__lastname = name[2]
        else:
            self.__midname = ''
            self.__lastname = name[1]
        self.__birthdate = ''

    def getName(self):
        """Returns self's full name"""
        if self.__midname != '':
            return f'{self.__name} {self.__midname} {self.__lastname}'
        else:
            return f'{self.__name} {self.__lastname}'

    def getLastName(self):
        """Returns self's last name"""
        return self.__lastname

    def setBirthday(self, birthdate):
        """Assumes birthdate is of type datetime.date Sets self's birthday to birthdate"""
        self.__birthdate = birthdate
    
    def getBirthday(self):
        """Assumes birthdate is of type datetime.date Sets self's birthday to birthdate"""
        return f'{self.__birthdate.year}-{self.__birthdate.month:02}-{self.__birthdate.day:02}'

    def getAge(self):
        """Returns self's current age in years"""
        today_date = datetime.date.today()
        year_now = today_date.year
        return year_now - self.__birthdate.year
        
    def __str__(self):
        """Returns self's name and birthday"""
        return f'{self.__name} {self.__lastname} {self.getBirthday()}'

today_date = datetime.date.today()
print(today_date)
print(today_date.day, today_date.month, today_date.year)
me = Person('Frederick Brooks')
him = Person('Barack Hussein Obama')
her = Person('Barbara Jane Liskov')
me.setBirthday(datetime.date(1931, 4, 19))
him.setBirthday(datetime.date(1961, 8, 4))
her.setBirthday(datetime.date(1939, 11, 7))
print(me)
print(him)
print(her)
print(me.getLastName())
print(him.getLastName())
print(her.getLastName())
print(me.getName(), 'is', me.getAge(), 'years old')
print(him.getName(), 'is', him.getAge(), 'years old')
print(her.getName(), 'is', her.getAge(), 'years old')
