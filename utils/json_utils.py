"""JSON工具函数"""
import json


def to_json(obj) -> str:
    """对象转JSON字符串"""
    return json.dumps(obj, ensure_ascii=False)


def from_json(s: str):
    """JSON字符串转对象"""
    return json.loads(s)
