class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq = Counter(nums[:k])
        curr_sum = sum(nums[:k])
        max_sum = curr_sum if len(freq) == k else 0
        for r in range(k, len(nums)):
            curr_sum += nums[r]
            curr_sum -= nums[r - k]
            freq[nums[r]] += 1
            freq[nums[r - k]] -= 1
            if freq[nums[r - k]] == 0:
                del freq[nums[r - k]]
            if len(freq) == k:
                max_sum = max(max_sum, curr_sum)
        return max_sum