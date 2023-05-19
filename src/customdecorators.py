import time
import logging
import functools


def help():
    print(""" Available decorators:
    @ttime: prints the time it took to execute the function
    @cache: caches the function's result
    @loginfo: logs the function's execution""")


help()


def cache(func):
    func_cache = {}

    def wrapper(*args):
        if args in func_cache:
            return func_cache[args]
        else:
            result = func(*args)
            func_cache[args] = result
            return result

    return wrapper


def ttime(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        total = round(time.time() - start_time, 3)
        print(f"Time {func.__name__}: {total} s.")
        return result

    return wrapper


logging.basicConfig(level=logging.INFO)


def loginfo(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Executing {func.__name__}")
        result = func(*args, **kwargs)
        logging.info(f"Finished executing {func.__name__}")
        return result

    return wrapper
