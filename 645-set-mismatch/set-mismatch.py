class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums_set = set(nums)
        seen = set()
        dup = 0
        for num in nums:
            if num in nums_set and num not in seen:
                seen.add(num)
            else:
                dup = num
                break
        res = [dup]
        all_num_gen = (x for x in range(1, len(nums) + 1))
        found = 0
        for num in all_num_gen:
            if num not in nums_set:
                return res + [num]