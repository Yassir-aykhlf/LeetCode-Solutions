class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n < 10: return []
        m = 10
        base = 4
        mod = 10**9 + 7
        highest_pow = pow(base, m - 1, mod)
        to_int = {"A":0, "C":1, "G":2, "T":3}
        nums = [to_int[c] for c in s]
        dna_hash = 0
        seen = set()
        res = set()
        for i in range(m):
            dna_hash = (dna_hash * base + nums[i]) % mod
        seen.add(dna_hash)
        for i in range(1, n - m + 1):
            dna_hash = ((dna_hash - nums[i - 1] * highest_pow) * base + nums[i + m - 1]) % mod
            if dna_hash in seen:
                res.add(s[i: i + m])
            seen.add(dna_hash)
        return list(res)