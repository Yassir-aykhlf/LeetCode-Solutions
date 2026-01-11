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
        curr = slow
        prev = None
        while curr:
            curr_next = curr.next
            curr.next = prev
            prev = curr
            curr = curr_next
        r1, r2 = head, prev
        while r2.next:
            r1_next, r2_next = r1.next, r2.next
            r1.next = r2
            r2.next = r1_next
            r1, r2 = r1_next, r2_next