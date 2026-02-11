class Solution:
    def mergeArr(self, nums, l, mid, r):
        arr = []
        i = l
        j = mid
        while i < mid and j < r:
            if nums[i] < nums[j]:
                arr.append(nums[i])
                i += 1
            else:
                arr.append(nums[j])
                j += 1
        while i < mid:
            arr.append(nums[i])
            i += 1
        while j < r:
            arr.append(nums[j])
            j += 1
        nums[l : r] = arr

    def mergeSort(self, nums, l, r):
        if l >= r - 1:
            return
        mid = (l + r) // 2
        self.mergeSort(nums, l, mid)
        self.mergeSort(nums, mid, r)
        self.mergeArr(nums, l, mid, r)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums, 0, len(nums))
        return nums