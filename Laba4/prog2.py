def catcher(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print("Ошибка:", e)
    return wrapper
def div(a, b):
    return a / b
div = catcher(div)
div(10, 2)
div(10, 0)