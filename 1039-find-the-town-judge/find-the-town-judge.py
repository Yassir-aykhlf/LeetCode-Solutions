class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        if not trust:
            return -1
        trust_map = defaultdict(set)
        for r in trust:
            trust_map[r[0]].add(r[1])
        if len(trust_map) != n - 1:
            return -1
        def everyone_trusts(i):
            for a, b in trust_map.items():
                if i not in b:
                    return False
            return True
        for i in range(1, n + 1):
            if i not in trust_map and everyone_trusts(i):
                return i
        return -1