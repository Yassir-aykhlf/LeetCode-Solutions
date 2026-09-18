class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        return "".join((c * count[c] for c in (sorted(count.keys(), key=lambda x: count[x], reverse=True))))