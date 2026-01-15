class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        _sum_count = {0: 1}
        curr_sum = 0
        count = 0
        for num in nums:
            curr_sum += num
            target = curr_sum - k
            if target in _sum_count:
                count += _sum_count[target]
            _sum_count[curr_sum] = _sum_count.get(curr_sum, 0) + 1
        return count