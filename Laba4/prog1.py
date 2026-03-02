def make_checker(min_val, max_val):
    def checker(x):
        if min_val <= x <= max_val:
            print(f"{x} в диапазоне")
            return True
        else:
            print(f"{x} вне диапазона")
            return False
    return checker
check = make_checker(0, 10)
check(5)
check(15)