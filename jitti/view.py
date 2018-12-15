from model import Football,FileImport

def router(route):
    if route == 'file':
        menu_choice = file()
        return menu_choice
    elif route == 'menu':
        menu_choice = menu()
        return menu_choice
    elif route == 'summary':
        menu_choice = summary()
        return menu_choice
    elif route == 'enter_result':
        menu_choice = enter_result()
        return menu_choice
    elif route == 'quit':
        exit('Bye')    

def file():
    name = input("Please enter a file name: ")
    data = FileImport(name)
    global data_list
    data_list_raw = data.read()
    data_list = []
    for data in data_list_raw:
        data_list.append(Football(data[1],data[0]))
    menu_choice = menu()
    return menu_choice

def menu():
    print('(s)how simmary (e)nter results (q)uit: ', end='')
    menu_choice = {
        's' : 'summary',
        'e' : 'enter_result',
        'q' : 'quit'
    }
    return menu_choice

def summary():
    for team in data_list:
        print(team)
    menu_choice = menu()
    return menu_choice

def enter_result():
    result = input('Enter a result: ')
    result = result.split(' ')
    if result[1] == 'won':
        for i in data_list:
            if i.get_short_name() == result[0]:
                i.won()
        for i in data_list:
            if i.get_short_name() == result[2]:
                i.lose()
    elif result[1] == 'drew':
        for i in data_list:
            if i.get_short_name() == result[0]:
                i.drew()
        for i in data_list:
            if i.get_short_name() == result[2]:
                i.drew()
    elif result[1] == 'losed':
        for i in data_list:
            if i.get_short_name() == result[0]:
                i.lose()
        for i in data_list:
            if i.get_short_name() == result[2]:
                i.won()
    else:
        print('Input Error')
    menu_choice = menu()
    return menu_choice

    