class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_str = [str(n) for n in nums]
        nums_str.sort(key=cmp_to_key(lambda a, b: -1 if a + b > b + a else 1))
        res = ''.join(nums_str)
        return "0" if res[0] == "0" else res