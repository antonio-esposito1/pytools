import timeit
def timer(func, *args):
    start = timeit.default_timer()
    for i in range(1000):
        func(*args)
    return timeit.default_timer() - start
