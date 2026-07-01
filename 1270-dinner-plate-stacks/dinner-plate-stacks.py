class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stack = []
        self.leftmost = []

    def push(self, val: int) -> None:
        while self.stack and not self.stack[-1]:
            self.stack.pop()
        while self.leftmost and self.leftmost[0] >= len(self.stack):
            heapq.heappop(self.leftmost)
        if self.leftmost:
            idx = self.leftmost[0]
            self.stack[idx].append(val)
            if self.capacity == len(self.stack[idx]):
                heapq.heappop(self.leftmost)
        else:
            if not self.stack or len(self.stack[-1]) == self.capacity:
                self.stack.append([val])
            else:
                self.stack[-1].append(val)

    def pop(self) -> int:
        while self.stack and not self.stack[-1]:
            self.stack.pop()
        if self.stack and self.stack[-1]:
            val = self.stack[-1].pop()
            return val
        return -1

    def popAtStack(self, index: int) -> int:
        while self.stack and not self.stack[-1]:
            self.stack.pop()
        if index >= len(self.stack) or len(self.stack[index]) == 0:
            return -1
        val = self.stack[index].pop()
        if len(self.stack[index]) == self.capacity - 1:
            heapq.heappush(self.leftmost, index)
        return val

# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)