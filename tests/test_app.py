import app


def test_fib_zero():
    assert app.fib(0) == 0


def test_fib_one():
    assert app.fib(1) == 1


def test_fib_seven():
    assert app.fib(7) == 13


def test_greet():
    assert app.greet("张三") == "Hello, 张三!"
