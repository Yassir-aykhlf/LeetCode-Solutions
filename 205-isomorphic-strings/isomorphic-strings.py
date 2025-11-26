class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_t = {}
        t_s = {}
        for s_c, t_c in zip(s, t):
           if (s_c in s_t and s_t[s_c] != t_c) or (t_c in t_s and t_s[t_c] != s_c):
            return False 
           s_t[s_c] = t_c
           t_s[t_c] = s_c
        return True