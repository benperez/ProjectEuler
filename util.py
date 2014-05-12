from time import time

def timed(func):
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        elapsed = time() - start
        print "%s found %s after %s seconds" % (func.func_name, result, elapsed)
        return result
    return wrapper
