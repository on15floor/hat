from datetime import datetime


def print_func_duration(func):
    """ Выводит время выполнения функции
    :param func: Функция
    :return: None
    """

    def inner(*args, **kwargs):
        start_time = datetime.now()
        # print(f'[i]> {func.__name__}() start: {start_time.strftime("%Y-%m-%d, %H:%M:%S")}')
        res = func(*args, **kwargs)
        stop_time = datetime.now()
        # print(f'[i]> {func.__name__}() stop: {stop_time.strftime("%Y-%m-%d, %H:%M:%S")}')
        exec_time = stop_time - start_time
        print(f'[i]> {func.__name__}() execution time: {exec_time.seconds * 1000 + exec_time.microseconds / 1000}ms')
        return res

    return inner


class PrintFuncDuration(object):
    """ Выводит время исполнения функции. Возможно применение к рекурсивным функциям
    """
    def __init__(self, f):
        self.f = f
        self.active = False

    def __call__(self, *args, **kwargs):
        if self.active:
            return self.f(*args, **kwargs)
        start_time = datetime.now()
        self.active = True
        res = self.f(*args, **kwargs)
        end_time = datetime.now()
        self.active = False
        exec_time = end_time - start_time
        print(f'[i]> {self.f.__name__}() execution time: {exec_time.seconds * 1000 + exec_time.microseconds / 1000}ms \n')
        return res
