def write(surname, name, telephone, description):
    import codecs
    with codecs.open('PhoneBook.txt', 'a', "utf-8") as l:
        l.write(f'{surname}' + '\n')
        l.write(f'{name}' + '\n')
        l.write(f'{telephone}' + '\n')
        l.write(f'{description}' + '\n')
        l.write(f'' + '\n')