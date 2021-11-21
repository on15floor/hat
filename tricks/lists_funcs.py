def list_get_intersections(input_list: list, input_another_list: list) -> list:
    """ Функция возвращает лист, состоящий из пересечения двух листов """
    return [k for k in input_list if k in input_another_list]
