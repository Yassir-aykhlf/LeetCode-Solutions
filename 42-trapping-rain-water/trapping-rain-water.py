class Solution:
    def trap(self, height: List[int]) -> int:
        n= len(height)
        res = 0
        l = 0
        r = n - 1
        maxL = height[l]
        maxR = height[r]
        while l < r:
            if height[l] < height[r]:
                l += 1
                maxL = max(maxL, height[l])
                res += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                res += maxR - height[r]
        return res