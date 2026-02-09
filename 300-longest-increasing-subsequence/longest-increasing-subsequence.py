"""
Input: [10,9,2,5,3,7,101,18]
state: []
[10]->[9]->[2]->[2,5]->[2,3]->[2,3,7]->[2,3,7,101]->[2,3,7,18]
LIS len = len(state)
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        state = []
        for n in nums:
            idx = bisect.bisect_left(state, n)
            if idx == len(state):
                state.append(n)
            else:
                state[idx] = n
        return len(state)