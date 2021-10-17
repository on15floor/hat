from utils.generators import random_digits_list_generator
from utils.decorators import print_func_duration


def find_smallest(some_list: list) -> int:
    """ Функция для поиска наименьшего элемента в списке
    :param some_list: Список
    :return: Индекс наименьшего элемента в списке
    """
    smallest = some_list[0]
    smallest_index = 0
    for i in range(1, len(some_list)):
        if some_list[i] < smallest:
            smallest = some_list[i]
            smallest_index = i
    return smallest_index


@print_func_duration
def selection_sort(some_list: list) -> str:
    """ Функция сортировки выбором
    Скорость выполнения: O(n*n), n=len(some_list)
    :param some_list: Исходный список для сортировки
    :return: Отсортированный список
    """
    _iter = 0  # кол-во итераций
    sorted_list = []
    for i in range(len(some_list)):
        _iter += 2  # т.к. в функции по поиску элемента, мы опять проходим список
        smallest = find_smallest(some_list)
        sorted_list.append(some_list.pop(smallest))
    res = f'[Selection Sort]> List was sorted with {_iter} iteration: {sorted_list[:10]}...'
    return res


if __name__ == '__main__':
    some_l = random_digits_list_generator(100)

    print(selection_sort(some_list=some_l))
