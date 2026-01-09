class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_t = {}
        t_s = {}
        for _s, _t in zip(s, t):
            if _s in s_t and s_t[_s] != _t or _t in t_s and t_s[_t] != _s:
                return False
            s_t[_s] = _t
            t_s[_t] = _s
        return True