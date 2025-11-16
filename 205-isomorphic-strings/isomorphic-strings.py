class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_t = {}
        t_s = {}
        for s_, t_ in zip(s, t):
            if s_ in s_t and s_t[s_] != t_:
                return False
            if t_ in t_s and t_s[t_] != s_:
                return False
            s_t[s_] = t_
            t_s[t_] = s_
        return True