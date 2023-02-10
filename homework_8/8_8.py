import time

def time_func(function):
    def counter(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        end_time = time.time()
        print(f'Time taken to execute {function.__name__}: {end_time - start_time} seconds')
        return result
    return counter

@time_func
def some_func():
    time.sleep(3)
    return

some_func()






