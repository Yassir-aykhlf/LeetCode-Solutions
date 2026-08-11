class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        _state = defaultdict(int)
        l = 0
        _max = 0
        _len = len(fruits)
        for r in range(_len):
            _state[fruits[r]] += 1
            while len(_state) > 2:
                _state[fruits[l]] -= 1
                if _state[fruits[l]] == 0:
                    del _state[fruits[l]]
                l += 1
            _max = max(_max, r - l + 1)
        return _max