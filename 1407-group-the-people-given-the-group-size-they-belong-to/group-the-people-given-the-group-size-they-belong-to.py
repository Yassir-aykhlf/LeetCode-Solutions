class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        bucket = defaultdict(list)
        res = []
        for id_, size_ in enumerate(groupSizes):
            if len(bucket[size_]) >= size_:
                res.append(bucket[size_])
                bucket[size_] = []
            bucket[size_].append(id_)
        for g in bucket.values():
            res.append(g)
        return res