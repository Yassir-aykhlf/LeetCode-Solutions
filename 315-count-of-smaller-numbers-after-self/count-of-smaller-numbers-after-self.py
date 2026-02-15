class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        counts = [0] * len(nums)
        indexed_nums = list(enumerate(nums))

        def merge(left, right):
            merged = []
            l, r = 0, 0
            right_counter = 0
            while l < len(left) and r < len(right):
                if right[r][1] < left[l][1]:
                    merged.append(right[r])
                    right_counter += 1
                    r += 1
                else:
                    merged.append(left[l])
                    counts[left[l][0]] += right_counter
                    l += 1
            while l < len(left):
                merged.append(left[l])
                counts[left[l][0]] += right_counter
                l += 1
            while r < len(right):
                merged.append(right[r])
                r += 1
            return merged

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            return merge(left, right)

        merge_sort(indexed_nums)
        return counts