class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = collections.defaultdict(list)
        res = []
        for _id, _size in enumerate(groupSizes):
            if len(groups[_size]) == _size:
                res.append(groups[_size])
                groups[_size] = []
            groups[_size].append(_id)
        for g in groups.values():
            res.append(g)
        return res