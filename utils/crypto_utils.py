"""加密工具函数"""
import hashlib


def md5(s: str) -> str:
    """MD5哈希"""
    return hashlib.md5(s.encode()).hexdigest()
