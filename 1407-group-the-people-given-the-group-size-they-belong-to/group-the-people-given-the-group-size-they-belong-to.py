class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        _size_id = defaultdict(list)
        res = []
        for _id, _size in enumerate(groupSizes):
            if len(_size_id[_size]) == _size:
                res.append(_size_id[_size])
                _size_id[_size] = []
            _size_id[_size].append(_id)
        for _g in _size_id.values():
            res.append(_g)
        return res