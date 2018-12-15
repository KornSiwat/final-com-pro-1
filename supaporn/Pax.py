class Pax():
    def __init__(self, pax_id=0, ori='', dest='', depart=0, arrive=0):
        self.__id = pax_id
        self.__ori = ori
        self.__dest = dest
        self.__depart = depart
        self.__arrive = arrive

    def __str__(self):
        return f'({self.__id},{self.__dest},{self.__depart}:00)'

    def get_id(self):
        return self.__id
    
    def get_ori(self):
        return self.__ori
    
    def get_dest(self):
        return self.__dest
    
    def get_depart(self):
        return self.__depart
    
    def get_arrive(self):
        return self.__arrive

if __name__ == "__main__":
    pax = Pax(1,"BKK", "CNX", 8,9)
    print(pax)