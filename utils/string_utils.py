"""字符串工具函数"""


def reverse(s: str) -> str:
    """反转字符串"""
    return s[::-1]


def uppercase(s: str) -> str:
    """转大写"""
    return s.upper()


def lowercase(s: str) -> str:
    """转小写"""
    return s.lower()


def capitalize(s: str) -> str:
    """首字母大写"""
    return s.capitalize()


def count_chars(s: str) -> int:
    """统计字符数"""
    return len(s)
