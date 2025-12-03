"""搜索工具函数"""


def linear_search(lst: list, target) -> int:
    """线性搜索"""
    for i, item in enumerate(lst):
        if item == target:
            return i
    return -1
