def view_phone(data):
    print(data)

def inpt():
    act = int(input('Выберите действие 1 - поиск, 2 - добавление: '))
    if act == 1:
        some_str = input('Введите фамилию для поиска номера ')
    elif act == 2:
        some_str = input('Введите данные для добавления в справочник (Фамилию Имя Телефон Описание): ')
    else:
        print('Введите цифру 1 или 2')
    return some_str, act

def view_data(str_number):
    q = str_number
    for i in range(q,q+4):
     with open('PhoneBook.txt',encoding="utf8") as file:
      print(file.readlines()[i])