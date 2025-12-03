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
