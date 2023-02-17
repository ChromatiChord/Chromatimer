from time import perf_counter

def decorator_timer(output=False):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = perf_counter()
            func(*args, **kwargs)
            if output:
                print(f"Function took {perf_counter() - start_time}s")
        return wrapper
    return decorator