from utils.decorators import print_func_duration


@print_func_duration
def binary_search(some_list: list, searching_item: int) -> str:
    """ Функция осуществляет бинарный поиск
    Скорость выполнения: O(log(n)), n=len(some_list)
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
