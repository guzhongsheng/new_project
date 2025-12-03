"""文件工具函数"""
import os


def file_exists(path: str) -> bool:
    """判断文件是否存在"""
    return os.path.isfile(path)
