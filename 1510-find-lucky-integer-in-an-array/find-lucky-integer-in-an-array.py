class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = collections.Counter(arr)
        res = []
        for num in arr:
            if freq[num] == num:
                res.append(num) 
        return sorted(res)[-1] if res else -1