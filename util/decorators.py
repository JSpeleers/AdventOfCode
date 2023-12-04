import time


def aoc_solution(year, day, part):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print(f"{year}/{day:02} p{part}:\t{result}")
            return result

        return wrapper

    return decorator


def aoc_timed_solution(year, day, part):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            print(f"{year}/{day:02} p{part}:\t{result}\t(took {(time.time() - start_time):.3f} s)")
            return result

        return wrapper

    return decorator
