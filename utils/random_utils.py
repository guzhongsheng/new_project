"""随机工具函数"""
import random


def random_int(a: int, b: int) -> int:
    """生成随机整数"""
    return random.randint(a, b)


def random_float(a: float, b: float) -> float:
    """生成随机浮点数"""
    return random.uniform(a, b)
