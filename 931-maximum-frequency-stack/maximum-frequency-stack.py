class FreqStack:
    def __init__(self):
        self.max_freq = 0
        self.freq_groups = {}
        self.freq = {}

    def push(self, val: int) -> None:
        f = self.freq.get(val, 0) + 1
        self.freq[val] = f
        self.max_freq = max(self.max_freq, f)
        if f not in self.freq_groups:
            self.freq_groups[f] = []
        self.freq_groups[f].append(val)

    def pop(self) -> int:
        if not self.freq_groups:
            raise IndexError("pop from empty list")
        index = self.max_freq
        val = self.freq_groups[index].pop()
        self.freq[val] -= 1
        if not self.freq_groups[index]:
            self.max_freq -= 1
        return val