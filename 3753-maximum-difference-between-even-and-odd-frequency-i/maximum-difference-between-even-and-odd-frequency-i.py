class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)
        items = [(f, c) for c, f in freq.items()]
        items.sort(reverse=True)
        a1, a2 = 0, 0
        for i in range(len(items)):
            f, c = items[i]
            if f % 2 == 1:
                a1 = f
                break
        for i in range(len(items) -1, -1, -1):
            f, c = items[i]
            if f % 2 == 0:
                a2 = f
                break
        return a1 - a2