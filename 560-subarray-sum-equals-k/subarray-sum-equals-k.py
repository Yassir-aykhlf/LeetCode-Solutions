class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_to_count = {0: 1}
        curr_sum = 0
        count = 0
        for num in nums:
            curr_sum += num
            prev_sum = curr_sum - k
            if prev_sum in sum_to_count:
                count += sum_to_count[prev_sum]
            sum_to_count[curr_sum] = sum_to_count.get(curr_sum, 0) + 1
        return count