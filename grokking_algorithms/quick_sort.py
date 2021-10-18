from utils.decorators import PrintFuncDuration, print_func_duration

# Кол-во итераций
_iter = 0


def quick_sort_exec(some_list: list) -> list:
    """ Функция быстрой сортировки
    Скорость выполнения: O(n*log(n)), n=len(some_list)
    :param some_list: Исходный список для сортировки
    :return: Отсортированный список
    """
    global _iter
    _iter += 1
    if len(some_list) < 2:
        return some_list
    else:
        pivot = some_list[0]
        less = [i for i in some_list[1:] if i <= pivot]
        greater = [i for i in some_list[1:] if i > pivot]
        return quick_sort_exec(less) + [pivot] + quick_sort_exec(greater)


@print_func_duration
def quick_sort(some_list: list) -> str:
    sorted_list = quick_sort_exec(some_list)
    res = f'[Quick Sort]> List was sorted with {_iter} iteration: {sorted_list[:10]}...'
    return res
