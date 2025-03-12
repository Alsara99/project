def log_decorator(filename: str = None):
    """Декоратор для логирования результатов выполнения функции в файл."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)

                if filename:
                    with open(filename, "a", encoding='utf-8') as f:
                        f.write(f"{func.__name__} ok\n")
                else:
                    print(f"{func.__name__} ok")

                return result
            except Exception as err:
                data = f"{func.__name__} error: {err} Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, 'a', encoding='utf-8') as f:
                        f.write(f"{data}\n")
                else:
                    print(f"{data}")

            return None

        return wrapper

    return decorator
