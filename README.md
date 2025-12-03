# new_project
This is a project.

简单示例项目 — 一个带有命令行的小工具，包含两个功能：

- `greet`：打印问候语。
- `fib`：计算斐波那契数（从 0 开始）。

运行方法（Windows PowerShell）：

```powershell
# 创建虚拟环境并激活
python -m venv .venv
.\.venv\Scripts\Activate.ps1
# 安装依赖（如果有）
python -m pip install -r requirements.txt

# 运行示例：
python app.py greet --name 张三
python app.py fib 10

# 运行测试（需要安装 pytest）
pytest
```

文件列表：

- `app.py`：主程序，包含 `greet` 和 `fib` 函数以及命令行入口。
- `requirements.txt`：依赖（本例只列出 `pytest` 用于测试，可选）。
- `tests/test_app.py`：简单单元测试。
