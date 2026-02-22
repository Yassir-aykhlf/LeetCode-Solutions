class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a, b):
            if a + b > b + a:
                return -1
            else:
                return 1
        nums_str = [str(num) for num in nums]
        nums_str.sort(key=cmp_to_key(compare))
        res = ''.join(nums_str)
        return res[0] if res[0] == "0" else res