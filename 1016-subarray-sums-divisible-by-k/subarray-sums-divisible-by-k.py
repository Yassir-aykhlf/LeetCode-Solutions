class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = collections.defaultdict(int)
        prefix[0] = 1
        cur_sum = 0
        count = 0
        for num in nums:
            cur_sum += num
            cur_rem = cur_sum % k
            count += prefix[cur_rem]
            prefix[cur_rem] += 1 
        return count
        