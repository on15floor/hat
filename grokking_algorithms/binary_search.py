from utils.generators import arranged_digits_list_generator
from utils.decorators import print_func_duration


@print_func_duration
def simple_search(some_list, searching_item):
    """ Функция осуществляет обычный поиск
    :param some_list: Отсортированный список, состоящем из цифр
    :param searching_item: Искомый элемент
    :return: Найденный элемент
    """
    _iter = 0  # кол-во итераций
    for i in range(0, len(some_list)):
        _iter += 1
        guess = some_list[i]
        if guess == searching_item:
            res = f'[Simple Search]> Element {guess} found with {_iter} iteration.'
            return res


@print_func_duration
def binary_search(some_list, searching_item):
    """ Функция осуществляет бинарный поиск
    Скорость выполнения: log(len(some_list))
    :param some_list: Отсортированный список, состоящем из цифр
    :param searching_item: Искомый элемент
    :return: Найденный элемент
    """
    _iter = 0                  # кол-во итераций
    low = 0                    # нижняя часть границы поиска
    high = len(some_list) - 1  # верхняя часть границы поиска

    while low <= high:
        _iter += 1
        mid = round((low + high) / 2)
        guess = some_list[mid]
        if guess == searching_item:
            res = f'[Binary Search]> Element {mid} found with {_iter} iteration.'
            return res
        if guess > searching_item:
            high = mid - 1
        else:
            low = mid + 1
    return None


if __name__ == '__main__':
    some_l = arranged_digits_list_generator(1000)
    item = 999

    print(simple_search(some_list=some_l, searching_item=item))
    print(binary_search(some_list=some_l, searching_item=item))
