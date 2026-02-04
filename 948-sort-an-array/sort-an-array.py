class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeArr(arr, l, r):
            sortd = []
            i = l
            mid = (l + r) // 2
            j = mid + 1
            while i <= mid and j <= r:
                if arr[i] < arr[j]:
                    sortd.append(arr[i])
                    i += 1
                else:
                    sortd.append(arr[j])
                    j += 1
            while i <= mid:
                sortd.append(arr[i])
                i += 1
            while j <= r:
                sortd.append(arr[j])
                j += 1
            arr[l: r + 1] = sortd
        def mergeSort(arr, l, r):
            if l >= r:
                return
            mid = (l + r) // 2
            mergeSort(arr, l, mid)
            mergeSort(arr, mid + 1, r)
            mergeArr(arr, l, r)
        mergeSort(nums, 0, len(nums) - 1)
        return nums