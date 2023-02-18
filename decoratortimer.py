from time import perf_counter

def decorator_timer(interval='s'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = perf_counter()
            func(*args, **kwargs)
            time = perf_counter() - start_time

            if interval == 'ms':
                time *= 1_000
            elif interval == 'µs':
                time *= 1_000_000
            elif interval == 'ns':
                time *= 1_000_000_000
            else:
                if interval != "s":
                    raise Exception("Decorator timer input error. Accepted values: [\"s\",\"ms\",\"µs\",\"ns\"]")
            
            print(f"Function \'{func.__name__}\' took {round(time, 5)}{interval}")
        return wrapper
    return decorator