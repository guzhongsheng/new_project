"""JSON工具函数"""
import json


def to_json(obj) -> str:
    """对象转JSON字符串"""
    return json.dumps(obj, ensure_ascii=False)
