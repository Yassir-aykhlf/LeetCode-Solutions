class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        acc_index = {0: -1}
        longest_window = 0
        acc = 0
        for i, h in enumerate(hours):
            acc += 1 if h > 8 else -1
            if acc > 0:
                longest_window = i + 1
            elif acc - 1 in acc_index:
                longest_window = max(longest_window, i - acc_index[acc - 1])
            if acc not in acc_index:
                acc_index[acc] = i
        return longest_window