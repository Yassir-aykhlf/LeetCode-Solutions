class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        curr_sum = 0
        sum_to_count = {0:1}
        for num in nums:
            if num % 2:
                curr_sum += 1
            prev_sum = curr_sum - k
            if prev_sum in sum_to_count:
                count += sum_to_count[prev_sum]
            sum_to_count[curr_sum] = sum_to_count.get(curr_sum, 0) + 1
        return count