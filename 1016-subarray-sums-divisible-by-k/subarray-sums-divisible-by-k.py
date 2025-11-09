class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        rem_count = {0:1}
        cur_sum = 0
        count = 0
        for num in nums:
            cur_sum += num
            cur_rem = cur_sum % k
            if cur_rem in rem_count:
                count += rem_count[cur_rem]
            else:
                rem_count[cur_rem] = 0
            rem_count[cur_rem] += 1
        return count