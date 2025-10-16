# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        dummy = ListNode(-1)
        cur = dummy
        while any(lst for lst in lists):
            min_val = float('inf')
            min_idx = -1
            for i in range(len(lists)):
                if lists[i] and lists[i].val < min_val:
                    min_val = lists[i].val
                    min_idx = i
            if min_idx != -1:
                cur.next = lists[min_idx]
                cur = cur.next
                lists[min_idx] = lists[min_idx].next
        return dummy.next