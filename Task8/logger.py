from data_create import input_user_data

def input_data():
    name, surname, phone, adress = input_user_data()
    var = int(input(f'\nВ каком виде записать данные? \n'
                    f'1 Вариант: \n'
                    f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{adress}\n\n'
                    f'2 Вариант: \n'
                    f'{name};{surname};{phone};{adress}\n\n'
                    f'Ваш выбор:' ))

    if var == 1:
       with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
        file.write(f'{name}\n'
                  f'{surname}\n'
                  f'{phone}\n'
                  f'{adress}\n\n')                
    
    else:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{adress}\n\n')

    print(f'Данные добавлены в {var} файл')


def print_data():
    print('1 файл: ')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        data_list = list()
        j = 0
        for i in range(len(data)):
            if data[i] == '\n':
                data_list.append(''.join(data[j:i]))
                j = i
        print(''.join(data_list))
    print('2 файл: ')    
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data = list(file.readlines())
        print(''.join(data))






def delete_data():
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        X = input('Введите имя или фамилию для удаления: ')
        lines = file.readlines()
        with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
            for line in lines:
                if X in line:
                    print('Указанные данные удалены')
                else:
                    print(line)    
                    file.write(line)