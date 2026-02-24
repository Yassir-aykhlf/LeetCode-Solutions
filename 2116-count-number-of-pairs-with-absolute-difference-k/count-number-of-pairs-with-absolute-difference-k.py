class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)
        count = 0
        for num in freq.keys():
            target = num - k
            if target in freq:
                count += freq[target] * freq[num]
        return count