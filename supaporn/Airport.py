class Airport():
    def __init__(self, code='', num_planes=0):
        self.__code = code
        self.__num_planes = num_planes
        self.__out_pax_list = []
        self.__in_pax_list = []

    def add_pax(self, pax):
        if pax.get_ori() == self.__code:
            self.__out_pax_list.append(pax)
        elif pax.get_dest() == self.__code:
            self.__in_pax_list.append(pax)
    
    def count_out_pax(self, dest_out):
        count = 0
        for i in self.__out_pax_list:
            if i.get_dest() == dest_out:
                count += 1
        return count

    def print_out_pax(self):
        print('Out-Pax: ', end='')
        for pax in self.__out_pax_list:
            print(f'{pax}, ', end='')
        print('')
    
    def print_in_pax(self):
        print('In-Pax: ', end='')
        for pax in self.__in_pax_list:
            print(f'{pax}, ', end='')
        print('')

    def __str__(self):
        print(f'AIRPORT-{self.__code}: {len(self.__out_pax_list)}, {len(self.__in_pax_list)}, {self.__num_planes}')
        self.print_out_pax()
        self.print_in_pax()
        return ''
