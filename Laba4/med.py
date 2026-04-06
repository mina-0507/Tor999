def repeat(times=2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            original = func
            saved = wrapper
            globals()[func.__name__] = original
            
            result = None
            for i in range(times):
                print(f"--- Вызов {i+1} из {times} ---")
                result = original(*args, **kwargs)
            globals()[func.__name__] = saved
            return result
        return wrapper
    return decorator

@repeat(times=3)
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

print("=== РЕЗУЛЬТАТ ===")
print(f"factorial(5) = {factorial(5)}")