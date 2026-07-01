class FreqStack:

    def __init__(self):
        self.cursor = 0
        self.freq = defaultdict(int)
        self.freq_stacks = defaultdict(list)

    def push(self, val: int) -> None:
        self.freq[val] += 1
        freq = self.freq[val]
        self.freq_stacks[freq].append(val)
        self.cursor = max(self.cursor, freq)

    def pop(self) -> int:
        val = self.freq_stacks[self.cursor].pop()
        self.freq[val] -= 1
        if not self.freq_stacks[self.cursor]:
            self.cursor -= 1
            print(self.cursor)
        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()