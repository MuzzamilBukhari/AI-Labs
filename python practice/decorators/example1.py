import time
def cache(func):
    cache_value = {}
    print("ye sirf pehli bar print hoga")
    def wrapper(*args, **kwargs):
        print(cache_value)
        print(args)
        if args in cache_value:
            return cache_value[args]
        result = func(*args, **kwargs)
        cache_value[args] = result
        return result
    return wrapper


@cache
def long_running_function(a, b, **kwargs):
    time.sleep(4)
    print(kwargs)
    return a + b

print(long_running_function(2,3, hello="hey", bhai="altaf"))
print("ab agla")
print(long_running_function(2,3))
print("ab agla")
print(long_running_function(2,6))