"""转换工具函数"""


def to_int(s: str) -> int:
    """字符串转整数"""
    return int(s)


def to_float(s: str) -> float:
    """字符串转浮点数"""
    return float(s)


def to_bool(s: str) -> bool:
    """字符串转布尔"""
    return s.lower() in ('true', '1', 'yes')
