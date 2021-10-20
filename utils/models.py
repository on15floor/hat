from collections import defaultdict


class Graph:
    """ Модель работы с графами
    """
    def __init__(self):
        self.directed_graph = defaultdict(list)
        self.undirected_graph = defaultdict(list)

    def fill_simple_graph(self, graph_type: str) -> None:
        """ Метод наполняет объект данными для формирования обычного направленного графа
        :param graph_type: Тип графа для заполнения
        :return: None
        """
        data = [['you', 'alice'], ['you', 'bob'], ['you', 'claire'], ['bob', 'anuj'], ['bob', 'peggy'],
                ['alice', 'peggy'], ['claire', 'thom'], ['claire', 'jonny']]
        for g in data:
            if graph_type == 'undirected_graph':
                self.add_undirected_graph(g[0], g[1])
            elif graph_type == 'directed_graph':
                self.add_directed_graph(g[0], g[1])

    def add_undirected_graph(self, node, adjacent_node) -> None:
        """ Добавления узла в направленный граф
        :param node: Узел
        :param adjacent_node: Соседний узел
        :return: None
        """
        self.directed_graph[node].append(adjacent_node)
        self.directed_graph[adjacent_node].append(node)

    def add_directed_graph(self, node, adjacent_node) -> None:
        """ Добавления узла в НЕ направленный граф
        :param node: Узел
        :param adjacent_node: Соседний узел
        :return: None
        """
        self.directed_graph[node].append(adjacent_node)

    def add_endpoint_to_directed_graph(self) -> None:
        """ Добавляет к словарю с направленным графом конечные точки
        :return: None
        """
        end_point = {}
        for v in self.directed_graph.values():
            for i in v:
                if i not in self.directed_graph.keys():
                    end_point[i] = []
        self.directed_graph.update(end_point)

    @property
    def get(self):
        """ Метод возвращает сформированный граф
        :return:
        """
        if self.directed_graph:
            self.add_endpoint_to_directed_graph()
            return dict(self.directed_graph)
        elif self.undirected_graph:
            return dict(self.undirected_graph)
        else:
            return None
