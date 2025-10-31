class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_len = 0
        state = collections.defaultdict(int)
        l = 0
        for r in range(len(fruits)):
            state[fruits[r]] += 1
            while len(state) > 2:
                state[fruits[l]] -= 1
                if state[fruits[l]] == 0:
                    del state[fruits[l]]
                l += 1
            max_len = max(max_len, r - l + 1)
        return max_len