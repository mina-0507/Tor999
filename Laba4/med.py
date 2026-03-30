import functools

def catcher_with_logger(log_file=None):
    """Декоратор с опциональным параметром"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"Ошибка: {e}")
                if log_file:
                    with open(log_file, 'a') as f:
                        f.write(f"{e}\n")
                return None
        return wrapper
    return decorator

def make_checker(min_val, max_val):
    @catcher_with_logger("errors.log")
    def checker(x):
        if min_val <= x <= max_val:
            print(f"{x} в диапазоне")
            return True
        print(f"{x} вне диапазона")
        return False
    return checker


@catcher_with_logger("errors.log")
def factorial(n):
    if n < 0:
        raise ValueError("Отрицательное число")
    return 1 if n == 0 else n * factorial(n-1)


check = make_checker(0, 10)
check(5)
check(15)
check("abc")

print(factorial(5))
factorial(-3)