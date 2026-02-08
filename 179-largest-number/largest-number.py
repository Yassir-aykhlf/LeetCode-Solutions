from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_str = [str(n) for n in nums]
        def compare(i, j):
            if i + j > j + i:
                return -1
            elif j + i > i + j:
                return 1
            return 0
        nums_str.sort(key=cmp_to_key(compare))
        result = ''.join(nums_str)
        return "0" if result[0] == "0" else result