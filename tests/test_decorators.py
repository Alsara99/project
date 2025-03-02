from src.decorators import log_decorator


def test_exception_log_decorator(capsys):
    @log_decorator()
    def my_function(x, y):
        print(x + y)
    my_function(1, '2')
    captured = capsys.readouterr()
    assert captured.out == "my_function error: unsupported operand type(s) for +: 'int' and 'str' Inputs: (1, '2'), {}\n"


def test_console_log_decorator(capsys):
    @log_decorator(filename="")
    def my_function(x, y):
        return x+y
    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == ('my_function ok\n')


def test_file_log_decorator():
    @log_decorator(filename="mylog.txt")
    def my_function(x, y):
        return x + y
    my_function(1, 2)
    with open("mylog.txt", 'r', encoding='utf-8') as f:
        data = f.read()
        assert data == "my_function ok\n"
