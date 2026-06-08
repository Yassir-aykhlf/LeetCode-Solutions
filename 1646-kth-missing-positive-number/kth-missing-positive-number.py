class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        seen = set(arr)
        count = 0
        i = 1
        while True:
            if i not in seen:
                count += 1
                if count == k:
                    return i
            i += 1
        return -1