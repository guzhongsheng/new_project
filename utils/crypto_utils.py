"""加密工具函数"""
import hashlib


def md5(s: str) -> str:
    """MD5哈希"""
    return hashlib.md5(s.encode()).hexdigest()


def sha256(s: str) -> str:
    """SHA256哈希"""
    return hashlib.sha256(s.encode()).hexdigest()
