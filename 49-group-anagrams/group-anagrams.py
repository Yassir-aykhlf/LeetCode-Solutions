class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for str_ in strs:
            key = ''.join(sorted(str_))
            if key not in groups:
                groups[key] = []
            groups[key].append(str_)
        return [lst for lst in groups.values()]