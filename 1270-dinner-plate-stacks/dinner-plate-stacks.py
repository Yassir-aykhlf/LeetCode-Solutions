class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = []
        self.available = []

    def push(self, val: int) -> None:
        while self.available and self.available[0] >= len(self.stacks):
            heappop(self.available)
        if self.available:
            idx = self.available[0]
            self.stacks[idx].append(val)
            if len(self.stacks[idx]) == self.capacity:
                heappop(self.available)
        else:
            self.stacks.append([val])
            if self.capacity > 1:
                heappush(self.available, len(self.stacks) - 1)

    def pop(self) -> int:
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()
        if not self.stacks:
            return -1
        val = self.stacks[-1].pop()
        if len(self.stacks[-1]) == self.capacity - 1:
            heappush(self.available, len(self.stacks) -1)
        return val

    def popAtStack(self, index: int) -> int:
        if index < 0 or index >= len(self.stacks) or not self.stacks[index]:
            return -1
        val = self.stacks[index].pop()
        if len(self.stacks[index]) == self.capacity - 1:
            heappush(self.available, index)
        return val