def caching_fibonacci():
    """Створює функцію fibonacci(n) із кешем і повертає її.

    Кеш зберігається в замиканні, тому результати обчислень
    запам'ятовуються між викликами fibonacci.
    """
    # Кеш створюється тут, а не всередині fibonacci, щоб
    # замикання зберігало його між викликами
    cache = {}

    def fibonacci(n):
        # Базові випадки: F(n) = 0 для n <= 0 та F(1) = 1
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        # Значення вже обчислене: беремо його з кешу
        elif n in cache:
            return cache[n]
        # Значення ще немає: обчислюємо рекурсивно та зберігаємо в кеш
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]

    # Повертаємо саму функцію (без виклику), а не її результат
    return fibonacci


# Приклад використання
fib = caching_fibonacci()
print(fib(10))  # 55
print(fib(15))  # 610