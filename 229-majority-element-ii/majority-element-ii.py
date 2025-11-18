class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        k = len(nums) // 3
        freq = Counter(nums)
        return [num for num in freq if freq[num] > k]