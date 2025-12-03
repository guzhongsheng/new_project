"""日期时间工具函数"""
from datetime import datetime


def now() -> str:
    """获取当前时间"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def today() -> str:
    """获取今天日期"""
    return datetime.now().strftime("%Y-%m-%d")
