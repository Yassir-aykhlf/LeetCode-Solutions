# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow
        prev= None
        while mid:
            mid_nxt = mid.next
            mid.next = prev
            prev = mid
            mid = mid_nxt
        r1, r2 = head, prev
        while r2.next:
            r1_next = r1.next
            r2_next = r2.next
            r1.next = r2
            r2.next = r1_next
            r1 = r1_next
            r2 = r2_next