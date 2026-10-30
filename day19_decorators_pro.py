from functools import wraps
#
# def retry(retries=3):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             for i in range(1, retries + 1):
#                 try:
#                     return func(*args, **kwargs)
#                 except Exception as e:
#                     print(f'Ошибка {e}! Осталось попыток: {retries - i}')
#                 if i == retries:
#                     print('Попыток не осталось')
#                     raise e
#         return wrapper
#     return decorator

def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        if args not in cache:
            cache[args] = func(*args, **kwargs)
            return cache[args]
        else:
            print(f'[CACHE] Взято из кэша для {args}')
            return cache[args]
    return wrapper