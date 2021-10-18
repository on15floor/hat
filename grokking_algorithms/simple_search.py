from utils.decorators import print_func_duration


@print_func_duration
def simple_search(some_list: list, searching_item: int) -> str:
    """ Функция осуществляет обычный поиск
    Скорость выполнения: O(n), n=len(some_list)
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
