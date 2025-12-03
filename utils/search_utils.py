"""搜索工具函数"""


def linear_search(lst: list, target) -> int:
    """线性搜索"""
    for i, item in enumerate(lst):
        if item == target:
            return i
    return -1


def binary_search(lst: list, target) -> int:
    """二分搜索（要求列表已排序）"""
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
