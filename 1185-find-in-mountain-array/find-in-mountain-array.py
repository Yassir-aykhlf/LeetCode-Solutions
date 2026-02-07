# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    """
    Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target. If such an index does not exist, return -1.
    """
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        # find peak index
        lo, hi = 0, n - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if mountainArr.get(mid) > mountainArr.get(mid + 1):
                hi = mid
            else:
                lo = mid + 1
        peakIndex = hi
        if mountainArr.get(peakIndex) == target:
            peakIndex
        # search left side
        lo, hi = 0, peakIndex
        while lo <= hi:
            mid = (lo + hi) // 2
            if mountainArr.get(mid) == target:
                return mid           
            elif mountainArr.get(mid) > target:
                hi = mid - 1
            else:
                lo = mid + 1
        # search right side
        lo, hi = peakIndex, n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if mountainArr.get(mid) == target:
                return mid           
            elif mountainArr.get(mid) < target:
                hi = mid - 1
            else:
                lo = mid + 1
        # not found
        return -1