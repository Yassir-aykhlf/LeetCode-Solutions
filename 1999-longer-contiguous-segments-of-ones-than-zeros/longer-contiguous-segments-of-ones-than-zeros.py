class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        z_len = max_z = 0
        o_len = max_o = 0
        for r in range(len(s)):
            if s[r] == '0':
                z_len += 1
            else:
                max_z = max(max_z, z_len)
                z_len = 0
            if s[r] == '1':
                o_len += 1
            else:
                max_o = max(max_o, o_len)
                o_len = 0
        max_z = max(max_z, z_len)
        max_o = max(max_o, o_len)
        return max_o > max_z