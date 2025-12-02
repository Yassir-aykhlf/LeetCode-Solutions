class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = Counter(arr)
        max_num = -1
        for num in arr:
            if num == freq[num]:
                max_num = max(max_num, num)
        return max_num