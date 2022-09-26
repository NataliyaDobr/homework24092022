def serch_phone(surname):
    with open('PhoneBook.txt',encoding="utf8") as f:
         for f.num_line, line in enumerate(f):
            if surname in line:
              return (f.num_line)
    return('Такой фамилии в справочнике нет')


          
