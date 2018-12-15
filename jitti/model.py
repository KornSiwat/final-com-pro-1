class Football():

    def __init__(self,full_name='',short_name='',win=0,draw=0,lose=0):
        self.__full_name = full_name
        self.__short_name = short_name
        self.__win = win
        self.__draw = draw
        self.__lose = 0

    def __str__(self):
        return f'{self.__full_name},{self.__short_name},{self.__win},{self.__draw},{self.__lose}'

    def won(self):
        self.__win += 1

    def drew(self):
        self.__draw += 1

    def lose(self):
        self.__lose += 1

    def get_short_name(self):
        return self.__short_name

class FileImport():

    def __init__(self,file_name=''):
        self.__filename = file_name

    def read(self):
        if self.__filename == '':
            raise ValueError('Empty filename')
        raw = open(self.__filename, 'r')
        data = raw.read().splitlines()
        raw.close()
        data = [x.split(',') for x in data if x != '']
        return data
        
