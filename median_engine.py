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


def select_ahu(k, lst):
    if len(lst) is 1:
        return lst[0]
    a = lst[random.randrange(0, len(lst))]
    set1 = [t for t in lst if t < a]
    set2 = [t for t in lst if t == a]
    set3 = [t for t in lst if t > a]
    if len(set1) >= k:
        return select_ahu(k, set1)
    elif len(set1) + len(set2) >= k:
        return a
    return select_ahu(k - len(set1) - len(set2), set3)

def less(first, second, with_equal):
    if with_equal:
        return first <= second
    return first < second

@time_measure_decorator
def median_ahu_method(lst):
    l = len(lst)
    if l % 2 == 1:
        k = (l+1) / 2
        even = False
    else:
        k = l / 2
        even = True
    med = select_ahu(k, lst)
    if even:
        clst = lst
        count = 0
        first_loop = True
        while count < k:
            for c in clst:
                if count == k:
                    break
                if less(c, med, not first_loop):
                    count += 1
                    clst.remove(c)
            first_loop = False

        med = (med + min(clst)) / 2
    return med


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
        i += 1
    return ret




fig = plt.gcf()
step = 1001;

indices = numpy.arange(0.0, 50.0)
values_sort = [0]
values_numpy = [0]
values_stat = [0]
values_ahu = [0]
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
    time_before = time.time()
    result_ahu = median_ahu_method(lst)
    time_after = time.time()
    values_ahu.append(1 * (time_after - time_before))
    if result_sort != result_numpy or result_sort != result_stat or result_sort != result_ahu :
        raise exception
        print result_sort
        print result_numpy
        print result_stat
    count += step

plt.plot(indices, values_sort, 'r--')
plt.plot(indices, values_numpy, 'g--')
plt.plot(indices, values_stat, 'b--')
plt.plot(indices, values_ahu, 'm--')

# print median_with_sort(lst)
# print median_numpy(lst)
# print median_stat(lst)

plt.show()
