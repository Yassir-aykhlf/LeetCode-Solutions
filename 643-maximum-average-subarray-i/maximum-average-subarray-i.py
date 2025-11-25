class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_sum = sum(nums[:k])
        max_sum = cur_sum
        for r in range(k, len(nums)):
            cur_sum += nums[r]
            cur_sum -= nums[r - k]
            max_sum = max(max_sum, cur_sum)
        return max_sum / k