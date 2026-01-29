class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        """ O(n) """
        # i = 1
        # while i < len(arr) - 1:
        #     if arr[i - 1] < arr[i] > arr[i + 1]:
        #         return i
        #     i += 1
        """ O(log(n)) """
        lo, hi = 0, len(arr) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid] > arr[mid + 1]:
                hi = mid
            else:
                lo = mid + 1
        return hi