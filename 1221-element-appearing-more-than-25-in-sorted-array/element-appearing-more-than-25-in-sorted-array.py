class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        threshold = n * 0.25
        count = Counter(arr)
        for n in count.keys():
            if count[n] > threshold:
                return n
        return -1