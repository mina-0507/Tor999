def safe_methods(cls):
    original_methods = {}
    for name in cls.__dict__:
        method = getattr(cls, name)
        if callable(method):
            original_methods[name] = method
    
    for name, method in original_methods.items():
        def make_wrapper(m):
            def wrapper(self, *args, **kwargs):
                try:
                    return m(self, *args, **kwargs)
                except ZeroDivisionError:
                    print("Ошибка: деление на ноль")
                except IndexError:
                    print("Ошибка: индекс вне диапазона")
                except ValueError:
                    print("Ошибка: неверное значение")
                except Exception as e:
                    print(f"Ошибка: {e}")
            return wrapper
        setattr(cls, name, make_wrapper(method))
    
    return cls

@safe_methods
class Calculator:
    def divide(self, a, b):
        return a / b
    
    def get_item(self, lst, index):
        return lst[index]
    
    def to_int(self, value):
        return int(value)

print("=== ДЕКОРАТОР КЛАССА ===")
calc = Calculator()

print("1. Деление 10/2:")
print("   Результат:", calc.divide(10, 2))

print("\n2. Деление 10/0:")
print("   Результат:", calc.divide(10, 0))

print("\n3. Получение [1,2,3][1]:")
print("   Результат:", calc.get_item([1,2,3], 1))

print("\n4. Получение [1,2,3][10]:")
print("   Результат:", calc.get_item([1,2,3], 10))

print("\n5. Преобразование int('123'):")
print("   Результат:", calc.to_int("123"))

print("\n6. Преобразование int('abc'):")
print("   Результат:", calc.to_int("abc"))