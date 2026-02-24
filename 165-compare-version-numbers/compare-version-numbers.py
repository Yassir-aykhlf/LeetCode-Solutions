class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(num) for num in version1.split('.')]
        v2 = [int(num) for num in version2.split('.')]
        p1, p2 = 0, 0
        while p1 < len(v1) and p2 < len(v2):
            if v1[p1] < v2[p2]:
                return -1
            elif v1[p1] > v2[p2]:
                return 1
            p1 += 1
            p2 += 1
        while p1 < len(v1):
            if v1[p1] > 0:
                return 1
            p1 += 1
        while p2 < len(v2):
            if v2[p2] > 0:
                return -1
            p2 += 1
        return 0