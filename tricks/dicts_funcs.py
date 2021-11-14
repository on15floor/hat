def dict_not_null(input_dict: dict) -> dict:
    """ Функция исключает пары со значением null """
    return {k: v for k, v in input_dict.items() if v is not None}


def dict_only_required_params(input_dict: dict, required_params: list) -> dict:
    """ Функция оставляет в словари лишь те пары, которые есть в словаре required_params """
    return {k: input_dict[k] for k in input_dict if k in required_params}


def dict_mapping_data(input_dict: dict, mapping_dict: dict):
    """ Изменяет ключи исходного словаря на ключи dict_mapping """
    return {mapping_dict.get(k, k): v for k, v in input_dict.items()}
