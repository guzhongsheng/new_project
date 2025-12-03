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


def to_hex(n: int) -> str:
    """整数转十六进制"""
    return hex(n)


def to_binary(n: int) -> str:
    """整数转二进制"""
    return bin(n)


def celsius_to_fahrenheit(c: float) -> float:
    """摄氏度转华氏度"""
    return c * 9 / 5 + 32
