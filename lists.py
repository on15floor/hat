from tricks.lists_funcs import list_get_intersections


input_list = ['first_name', 'last_name', 'middle_name']
input_another_list = ['last_name']


if __name__ == '__main__':
    # Исключаем из словаря ключи со значением None
    print(list_get_intersections(input_list, input_another_list))
