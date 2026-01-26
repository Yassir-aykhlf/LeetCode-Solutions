class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res = [[arr[i], arr[i + 1]] for i in range(len(arr)-1)]
        group = defaultdict(list)
        for arr in res:
            group[arr[1] - arr[0]].append(arr)
        smallest = min(group.keys())
        return group[smallest]