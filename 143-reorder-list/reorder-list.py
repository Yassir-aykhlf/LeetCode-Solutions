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
        prev = None
        cur = slow
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        L1, L2 = head, prev
        while L2.next:
            L1_nxt, L2_nxt = L1.next, L2.next
            L1.next = L2
            L2.next = L1_nxt
            L1, L2 = L1_nxt, L2_nxt
