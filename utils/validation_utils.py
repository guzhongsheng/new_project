"""验证工具函数"""
import re


def is_email(s: str) -> bool:
    """验证邮箱格式"""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, s))
