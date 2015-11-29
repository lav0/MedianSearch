import numpy
import statistics
import random
import time
from TimeMeasureDecorator import time_measure_decorator
import matplotlib.pyplot as plt


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
    i = 0
    while i != count:
        ret.append(random.uniform(-1000, 1000))
        i = i + 1
    return ret



fig = plt.gcf()
#fig.add_subplot(111, aspect='equal')

#line = plt.Line2D((.1, .9), (.1, .9), marker='o', color='r')

#lst = generate_list_of_randoms(10 ** 7)
first = None
second = None

step = 1000;

indices = numpy.arange(0.0, 1000.0)
values_sort = [0]
values_numpy = [0]
values_stat = [0]
count = 10
for i in indices:
    if i == 0.0:
        continue
    lst = generate_list_of_randoms(count)
    time_before = time.time()
    result_sort = median_with_sort(lst)
    time_after = time.time()
    values_sort.append(1 * (time_after - time_before))
    time_before = time.time()
    result_numpy = median_numpy(lst)
    time_after = time.time()
    values_numpy.append(1 * (time_after - time_before))
    time_before = time.time()
    result_stat = median_stat(lst)
    time_after = time.time()
    values_stat.append(1 * (time_after - time_before))
    if result_sort != result_numpy or result_sort != result_stat:
        print result_sort
        print result_numpy
        print result_stat
    count += 1000

plt.plot(indices, values_sort, 'r--')
plt.plot(indices, values_numpy, 'g--')
plt.plot(indices, values_stat, 'b--')

# print median_with_sort(lst)
# print median_numpy(lst)
# print median_stat(lst)

plt.show()
