from grokking_algorithms.binary_search import binary_search
from grokking_algorithms.simple_search import simple_search
from grokking_algorithms.selection_sort import selection_sort
from grokking_algorithms.quick_sort import quick_sort
from utils.generators import random_digits_list_generator, arranged_digits_list_generator

# Сравнение алгоритмов поиска
arranged_digits_list = arranged_digits_list_generator(1000)
item = 999
print(simple_search(some_list=arranged_digits_list.copy(), searching_item=item))
print(binary_search(some_list=arranged_digits_list.copy(), searching_item=item))

# Сравнение алгоритмов сортировки
random_digits_list = random_digits_list_generator(1000)
print(selection_sort(some_list=random_digits_list.copy()))
print(quick_sort(some_list=random_digits_list.copy()))