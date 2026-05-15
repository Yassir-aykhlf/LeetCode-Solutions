class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write, read = 0, 0
        while read < len(nums):
            if nums[read] != val:
                nums[write] = nums[read]
                write += 1
            read += 1
        return write