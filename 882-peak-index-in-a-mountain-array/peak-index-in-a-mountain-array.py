class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        lo, hi = 1, len(arr) - 2
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid-1] < arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid-1] < arr[mid] < arr[mid+1]:
                lo = mid + 1
            else:
                hi = mid - 1