from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        def cmp(n1, n2):
            if str(n1) + str(n2) > str(n2) + str(n1):
                return -1
            else:
                return 1
        nums_ = sorted(nums, key=cmp_to_key(cmp))
        return "".join(str(n) for n in nums_) if nums_[0] else "0"