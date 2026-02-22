class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        arr_to_frac = {}
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                arr_to_frac[(arr[i], arr[j])] = arr[i] / arr[j]
        return sorted(arr_to_frac.items(), key=itemgetter(1))[k - 1][0]