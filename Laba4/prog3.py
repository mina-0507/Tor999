def catcher(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print("Ошибка:", e)
    return wrapper
def make_checker(min_val, max_val):
    def checker(x):
        if min_val <= x <= max_val:
            print(f"{x} подходит")
            return True
        else:
            print(f"{x} не подходит")
            return False
    return checker
check = make_checker(0, 10)
safe_check = catcher(check)

safe_check(5)
safe_check(15)
safe_check("abc")