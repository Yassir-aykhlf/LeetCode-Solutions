class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = {}
        largest = -1
        for num in arr:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
        for num in arr:
            if freq[num] == num:
                largest = max(largest, num)
        return largest