import os


def log_decorator(filename: str = None):
    """Декоратор для логирования результатов выполнения функции в файл."""
    def decorator(func):
        """Декоратор, который добавляет логирование результатов работы функции."""
        def wrapper(*args, **kwargs):
            """Обертка функции, выполняющая логирование и обработку ошибок."""
            try:
                result = func(*args, **kwargs)

                if filename:
                    if os.path.isfile(filename):
                        with open(filename, "a", encoding='utf-8') as f:
                            data = f"{func.__name__} ok\n"

                            f.write(data)
                    else:
                        print(f"{func.__name__} {result}\n")
                else:
                    print(f"{func.__name__} {result}")

                return result
            except Exception as err:
                if filename:
                    with open(filename, 'a', encoding='utf-8') as f:
                        data = f"{func.__name__} error: {err} Inputs: {args}, {kwargs}"

                        f.write(data)
                else:
                    print(f"{func.__name__} error: {err} Inputs: {args}, {kwargs}")

            return None

        return wrapper

    return decorator
