"""日期时间工具函数"""
from datetime import datetime


def now() -> str:
    """获取当前时间"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def today() -> str:
    """获取今天日期"""
    return datetime.now().strftime("%Y-%m-%d")


def year() -> int:
    """获取当前年份"""
    return datetime.now().year


def month() -> int:
    """获取当前月份"""
    return datetime.now().month


def day() -> int:
    """获取当前日"""
    return datetime.now().day


def weekday() -> int:
    """获取星期几 (0=周一, 6=周日)"""
    return datetime.now().weekday()


def is_leap_year(year: int) -> bool:
    """判断是否为闰年"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
