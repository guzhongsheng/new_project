"""计数器工具"""


class Counter:
    """简单计数器"""

    def __init__(self, start: int = 0):
        self.value = start

    def increment(self) -> int:
        """增加1"""
        self.value += 1
        return self.value

    def decrement(self) -> int:
        """减少1"""
        self.value -= 1
        return self.value
