class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            comb = numbers[l] + numbers[r]
            if comb == target:
                return [l + 1, r + 1]
            elif comb > target:
                r -= 1
            else:
                l += 1
        return [-1, -1]