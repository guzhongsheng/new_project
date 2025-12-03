"""列表工具函数"""


def sum_list(lst: list) -> int:
    """求和"""
    return sum(lst)


def max_list(lst: list):
    """最大值"""
    return max(lst)


def min_list(lst: list):
    """最小值"""
    return min(lst)


def avg_list(lst: list) -> float:
    """平均值"""
    return sum(lst) / len(lst) if lst else 0


def reverse_list(lst: list) -> list:
    """反转列表"""
    return lst[::-1]
