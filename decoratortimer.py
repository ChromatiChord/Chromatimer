from time import perf_counter

def decorator_timer(interval='s'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # runs the function and times the output
            start_time = perf_counter()
            func(*args, **kwargs)
            total_time = perf_counter() - start_time

            # determines what time inteval should be displayed
            if interval == 'ms':
                total_time *= 1_000
            elif interval == 'µs':
                total_time *= 1_000_000
            elif interval == 'ns':
                total_time *= 1_000_000_000
            else:
                if interval != "s":
                    raise Exception("Decorator timer input error. Accepted values: [\"s\",\"ms\",\"µs\",\"ns\"]")
            
            print(f"Function \'{func.__name__}\' took {round(total_time, 4)}{interval}.")
        return wrapper
    return decorator