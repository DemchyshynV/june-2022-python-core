import math
import time
import multiprocessing

def time_decor(func):
    def inner(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print(time.time() - start)

    return inner


def worker(num):
    res = str(math.sqrt(math.sqrt(math.sqrt((num / 2) * 5 / 15)))) + 'H'
    return res


@time_decor
def main_process():
    print('Main')
    numbers = range(10000000)
    with open('file1.txt', 'w') as file:
        for num in numbers:
            res = worker(num)
            print(res, file=file)

# main_process()

@time_decor
def mp():
    print('mp')
    count = multiprocessing.cpu_count()
    print(count, 'CPUs')
    with multiprocessing.Pool(count) as p:
        numbers = range(10000000)
        with open('file2.txt', 'w') as file:
            res = p.map(worker, numbers)
            for item in res:
                print(item, file=file)

mp()
