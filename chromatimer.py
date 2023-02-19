from time import perf_counter
import sys

def chromatimer(interval='s', decimals=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # runs the function and times the output
            start_time = perf_counter()
            func(*args, **kwargs)
            total_time = perf_counter() - start_time

            # determines what time interval should be displayed
            if interval == 'ms':
                total_time *= 1_000
            elif interval == 'µs':
                total_time *= 1_000_000
            elif interval == 'ns':
                total_time *= 1_000_000_000
            else:
                if interval != "s":
                    sys.tracebacklimit = 0
                    raise Exception(f"Decorator timer \'interval\' invalid input. Accepted values: [\"s\",\"ms\",\"µs\",\"ns\"]. (Function: {func.__name__})")
            
            if not isinstance(decimals, int) or decimals < 0:
                sys.tracebacklimit = 0
                raise Exception(f"Decorator timer \'decimals\' invalid input. Must be an integer greater than 0. (Function: {func.__name__})")

            print(f"Function \'{func.__name__}\' took {round(total_time, decimals)}{interval}.")
        return wrapper
    return decorator
    
    