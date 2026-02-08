class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        result = ''.join(sorted([str(n) for n in nums], key = cmp_to_key(lambda a, b: -1 if a + b > b + a else 1)))
        return "0" if result[0] == "0" else result