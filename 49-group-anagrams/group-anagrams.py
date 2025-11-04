class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = collections.defaultdict(list)
        for str_ in strs:
            code = ''.join(sorted(str_))
            group[code].append(str_)
        return [arr for arr in group.values()]