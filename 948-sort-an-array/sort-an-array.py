class Solution:
    """
    Given an array of integers nums, sort the array in ascending order and return it.
    You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.
    """
    def mergeArr(self, arr, l, r):
        tmp = []
        mid = (l + r) // 2
        i = l
        j = mid
        while i < mid and j < r:
            if arr[i] < arr[j]:
                tmp.append(arr[i])
                i += 1
            else:
                tmp.append(arr[j])
                j += 1
        while i < mid:
            tmp.append(arr[i])
            i += 1
        while j < r:
            tmp.append(arr[j])
            j += 1
        arr[l : r] = tmp
    def MergeSort(self, arr, l, r):
        if r - 1 <= l:
            return
        mid = (l + r) // 2
        self.MergeSort(arr, l, mid)
        self.MergeSort(arr, mid, r)
        self.mergeArr(arr, l, r)
    def sortArray(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums)
        self.MergeSort(nums, l, r)
        return nums