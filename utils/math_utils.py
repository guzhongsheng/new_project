"""数学工具函数"""


def add(a: int, b: int) -> int:
    """加法"""
    return a + b


def subtract(a: int, b: int) -> int:
    """减法"""
    return a - b


def multiply(a: int, b: int) -> int:
    """乘法"""
    return a * b


def divide(a: int, b: int) -> float:
    """除法"""
    if b == 0:
        raise ValueError("除数不能为0")
    return a / b


def power(base: int, exp: int) -> int:
    """幂运算"""
    return base ** exp


def modulo(a: int, b: int) -> int:
    """取模"""
    return a % b


def absolute(n: int) -> int:
    """绝对值"""
    return abs(n)
