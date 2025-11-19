class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        bucket = defaultdict(list)
        group = []
        for id_, size in enumerate(groupSizes):
            if len(bucket[size]) >= size:
                group.append(bucket[size])
                bucket[size] = []
            bucket[size].append(id_)
        for g in bucket.values():
            group.append(g)
        return group