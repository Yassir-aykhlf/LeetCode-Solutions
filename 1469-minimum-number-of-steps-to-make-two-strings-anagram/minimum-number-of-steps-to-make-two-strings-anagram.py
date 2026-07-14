class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_ = Counter(s)
        t_ = Counter(t)
        count = 0
        for c in s_:
            if t_[c] < s_[c]:
                count += max(t_[c], s_[c]) - min(t_[c], s_[c])
        return count