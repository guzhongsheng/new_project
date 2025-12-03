"""验证工具函数"""
import re


def is_email(s: str) -> bool:
    """验证邮箱格式"""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, s))


def is_phone(s: str) -> bool:
    """验证手机号格式"""
    pattern = r'^1[3-9]\d{9}$'
    return bool(re.match(pattern, s))


def is_url(s: str) -> bool:
    """验证URL格式"""
    pattern = r'^https?://[\w\.-]+\.\w+'
    return bool(re.match(pattern, s))


def is_numeric(s: str) -> bool:
    """验证是否为数字"""
    return s.isdigit()


def is_alpha(s: str) -> bool:
    """验证是否为字母"""
    return s.isalpha()
