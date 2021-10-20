from collections import deque
from utils.decorators import print_func_duration


# Проверка условия поиска
def person_is_seller(name: str) -> bool:
    return name[-1] == 'm'


@print_func_duration
def breadth_first_search(graph: dict, name: str) -> str:
    """ Функция осуществляет поиск в ширину по графу
    Скорость выполнения: O(V+E), V-количество вершин графа, E-количество ребер графа
    Граф, используемый в примере: anuj ←- bob ←--- you --→ claire -→ tom
                                           ↓        ↓        ↓
                                         peggy ←- alice    jonny
    :param graph: Граф
    :param name: Узел, с которого начнем поиск
    :return: bool
    """
    _iter = 0
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        _iter += 1
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                return f'[Breadth First Search] {person.capitalize()} +  is a mango seller! Find in {_iter} iteration.'
            else:
                search_queue += graph[person]
                searched.append(person)
    return f'[Breadth First Search]There is no mango sellers! Total iteration: {_iter}'
