def oper(s_tuple):
    if s_tuple[1] == 1:
        surname = s_tuple[0]
        return surname
    else:
        some_list = s_tuple[0].split()
        surname = some_list[0]
        name = some_list[1]
        telephone = some_list[2]
        description = some_list[3]
        return surname, name, telephone,description
    