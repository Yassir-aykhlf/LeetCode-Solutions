class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainders = defaultdict(int)
        remainders[0] = 1
        cur_sum = 0
        count = 0
        for num in nums:
            cur_sum += num
            cur_rem = cur_sum % k
            if cur_rem in remainders:
                count += remainders[cur_rem]
            remainders[cur_rem] += 1
        return count