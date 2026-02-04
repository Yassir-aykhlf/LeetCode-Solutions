# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # find peak
        n = mountainArr.length()
        lo, hi = 0, n - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if mountainArr.get(mid) > mountainArr.get(mid + 1):
                hi = mid
            else:
                lo = mid + 1
        peakIndex = hi
        if mountainArr.get(peakIndex) == target:
            return peakIndex
        # search left
        lo, hi = 0, peakIndex - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if mountainArr.get(mid) == target:
                return mid
            elif mountainArr.get(mid) > target:
                hi = mid - 1
            else:
                lo = mid + 1
        # search right
        lo, hi = peakIndex + 1, n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if mountainArr.get(mid) == target:
                return mid
            elif mountainArr.get(mid) < target:
                hi = mid - 1
            else:
                lo = mid + 1
        return -1