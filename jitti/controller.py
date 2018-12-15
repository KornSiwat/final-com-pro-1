from view import router

def start():
    route = ''
    menu_choice = router('file')
    while True:
        route = input('')
        while route not in menu_choice:
            print('please input valid choice',end='')
            route = input('')
        menu_choice = router(menu_choice[route])
    