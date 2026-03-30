import functools

def ErrorHandlingClass(cls):
    """Декоратор классов"""
    for name, method in cls.__dict__.items():
        if callable(method) and not name.startswith('__'):
            setattr(cls, name, _safe_wrapper(method))
        elif name == '__init__' and callable(method):
            setattr(cls, '__init__', _safe_wrapper(method))
    return cls

def _safe_wrapper(method):
    @functools.wraps(method)
    def wrapper(*args, **kwargs):
        try:
            return method(*args, **kwargs)
        except Exception as e:
            print(f"Ошибка в {method.__name__}: {e}")
            return None
    return wrapper


@ErrorHandlingClass
class RangeChecker:
    def __init__(self, min_val, max_val):
        self.min_val = min_val
        self.max_val = max_val
    
    def check(self, x):
        if self.min_val <= x <= self.max_val:
            print(f"{x} в диапазоне")
            return True
        print(f"{x} вне диапазона")
        return False
    
    def div(self, a, b):
        return a / b


checker = RangeChecker(0, 10)
checker.check(5)
checker.check(15)
checker.check("abc")
checker.div(10, 2)
checker.div(10, 0)