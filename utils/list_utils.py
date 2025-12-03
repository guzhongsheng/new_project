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


def unique_list(lst: list) -> list:
    """去重"""
    return list(set(lst))


def flatten(lst: list) -> list:
    """展平嵌套列表"""
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result
