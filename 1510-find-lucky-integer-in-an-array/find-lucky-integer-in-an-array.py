class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = collections.Counter(arr)
        res = -1
        for num in arr:
            if freq[num] == num:
                res = max(res, num) 
        return res