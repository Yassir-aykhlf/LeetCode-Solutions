class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = collections.Counter(arr)
        largest = -1
        for num in arr:
            if freq[num] == num:
                largest = max(largest, num)
        return largest