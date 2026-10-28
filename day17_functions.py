import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Функция {func.__name__} выполнилась за {end - start:.5f} секунд.")
        return result
    return wrapper

@timer
def add(x, y):
    return x + y

for i in range(10):
    print(add(i, i))

print("Как тебя зовут, функция?", add.__name__)
