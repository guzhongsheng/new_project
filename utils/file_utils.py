"""文件工具函数"""
import os


def file_exists(path: str) -> bool:
    """判断文件是否存在"""
    return os.path.isfile(path)


def dir_exists(path: str) -> bool:
    """判断目录是否存在"""
    return os.path.isdir(path)


def get_extension(path: str) -> str:
    """获取文件扩展名"""
    return os.path.splitext(path)[1]


def get_filename(path: str) -> str:
    """获取文件名"""
    return os.path.basename(path)


def get_dir(path: str) -> str:
    """获取目录路径"""
    return os.path.dirname(path)


def list_files(path: str) -> list:
    """列出目录中的文件"""
    return os.listdir(path)
