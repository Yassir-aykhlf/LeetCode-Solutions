class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        group = {}
        result = []
        for person, groupSize in enumerate(groupSizes):
            if groupSize not in group:
                group[groupSize] = []
            if len(group[groupSize]) == groupSize:
                result.append(group[groupSize])
                group[groupSize] = []
            group[groupSize].append(person)
        for g in group.values():
            result.append(g)
        return result