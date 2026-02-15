class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.total_count = 0
        
        def merge(left, right):
            l, r = 0, 0
            while l < len(left):
                while r < len(right) and left[l] > 2 * right[r]:
                    r += 1
                self.total_count += r
                l += 1
            
            merged = []
            l, r = 0, 0
            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    merged.append(left[l])
                    l += 1
                else:
                    merged.append(right[r])
                    r += 1
            
            merged.extend(left[l:])
            merged.extend(right[r:])
            return merged

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            return merge(left, right)

        merge_sort(nums)
        return self.total_count