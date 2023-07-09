from logger import input_data, print_data, delete_data

def interface():
    print('Добрый день! Это бот-помошник. \n' 
          'Что Вы хотите сделать? \n'
          '1 - Записать данные \n'
          '2 - Вывестии данные \n'
          '3 - Удалить данные ')

    command = int(input('Ваш выбор: '))

    while command < 1 or command > 3:
        command = int(input('Ошибка! Попробуйте ещё раз! Ваш Выбор: '))

    if command == 1:
        input_data()

    elif command == 2:
        print_data()


    elif command == 3:
        delete_data() 
     