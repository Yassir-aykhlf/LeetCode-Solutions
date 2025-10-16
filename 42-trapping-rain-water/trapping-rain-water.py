class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxL = height[0]
        maxR = height[n - 1]
        l = 0
        r = n - 1
        res = 0
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