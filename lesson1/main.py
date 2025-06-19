import datetime
import time


def running_time(func):
    def wrapper(num):
        start_time = time.time()
        result = func(num)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"זמן ריצה של הפונקציה: {execution_time:.6f} שניות")
        return result
    return wrapper

cached_results = {}
def cache(func):
    def wrapper(num,**kwargs):
        start_time = time.time()
        if num in cached_results:
            result = cached_results[num]
        else:
            result = func(num,**kwargs)
            cached_results[num]=result
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"זמן ריצה של הפונקציה: {execution_time:.6f} שניות")
        return result

    return wrapper

@cache
def fibonacci(num):
    if num == 1 or num == 2:
        return 1

    a, b = 1, 1
    for _ in range(3, num + 1):
        a, b = b, a + b

    return b


print(fibonacci(10000))
