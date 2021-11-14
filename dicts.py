from tricks.dicts_funcs import dict_not_null, dict_only_required_params, dict_mapping_data

input_dict = {
    'last_name': 'Ivanov',
    'first_name': 'Ivan',
    'middle_name': None,
}
dict_mapping = {
    'last_name': 'l_name',
    'first_name': 'f_name',
}
required_params = ['last_name', 'middle_name']

if __name__ == '__main__':
    # Исключаем из словаря ключи со значением None
    print(dict_not_null(input_dict))
    # Оставить в словаре только ключи из required_params
    print(dict_only_required_params(input_dict, required_params))
    # Mapping словаря
    print(dict_mapping_data(input_dict, dict_mapping))
