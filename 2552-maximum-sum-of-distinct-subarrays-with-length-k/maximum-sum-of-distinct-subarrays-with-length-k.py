class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        window = collections.Counter(nums[:k])
        cur_sum = sum(nums[:k])
        max_sum = cur_sum if len(window) == k else 0
        n = len(nums)
        for r in range(k, n):
            cur_sum += nums[r]
            cur_sum -= nums[r - k]
            window[nums[r]] += 1
            window[nums[r - k]] -= 1
            if window[nums[r - k]] == 0:
                del window[nums[r - k]]
            if len(window) == k:
                max_sum = max(max_sum, cur_sum)
        return max_sum