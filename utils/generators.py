import random


def arranged_digits_list_generator(length: int) -> list:
    """ Генератор упорядоченного списка, состоящего из цифр от 0 до length
    :param length: Длина списка
    :return: Упорядоченный список
    """
    return [i for i in range(0, length)]


def random_digits_list_generator(length: int) -> list:
    """ Генератор списка из случайных целых цифр от 0 до length
    :param length: Длина списка
    :return: Неупорядоченный список
    """
    return random.sample(range(0, length), length)
