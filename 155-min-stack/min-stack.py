class MinStack:

    def __init__(self):
        self._stack_val = []
        self._stack_min = []

    def push(self, val: int) -> None:
        self._stack_val.append(val)
        self._stack_min.append(val if not self._stack_min else min(val, self._stack_min[-1]))

    def pop(self) -> None:
        self._stack_val.pop()
        self._stack_min.pop()

    def top(self) -> int:
        return self._stack_val[-1] if self._stack_val else -1

    def getMin(self) -> int:
        return self._stack_min[-1] if self._stack_min else -1


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()