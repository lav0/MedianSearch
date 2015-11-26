import numpy
import statistics
import random
from TimeMeasureDecorator import time_measure_decorator


@time_measure_decorator
def median_with_sort(lst):
    middle = len(lst) / 2
    sorted_list = sorted(lst)
    if not len(sorted_list) % 2:
        return 0.5 * (sorted_list[middle - 1] + sorted_list[middle])
    return sorted_list[middle]


@time_measure_decorator
def median_numpy(lst):
    return numpy.median(numpy.array(lst))


@time_measure_decorator
def median_stat(lst):
    return statistics.median(lst)


def generate_list_of_randoms(count):
    ret = list()
    for i in range(count):
        ret.append(random.uniform(-1000, 1000))
    return ret


lst = generate_list_of_randoms(1000000)

print median_with_sort(lst)
print median_numpy(lst)
print median_stat(lst)