"""随机工具函数"""
import random


def random_int(a: int, b: int) -> int:
    """生成随机整数"""
    return random.randint(a, b)


def random_float(a: float, b: float) -> float:
    """生成随机浮点数"""
    return random.uniform(a, b)


def random_choice(lst: list):
    """从列表随机选择"""
    return random.choice(lst)


def shuffle(lst: list) -> list:
    """打乱列表"""
    result = lst.copy()
    random.shuffle(result)
    return result


def random_bool() -> bool:
    """随机布尔值"""
    return random.choice([True, False])
