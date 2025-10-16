# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast =head
        while fast and fast.next:
            slow = slow.next
            fast =fast.next.next
        prev = None
        cur = slow
        while cur:
            nxt = cur.next
            cur.next= prev
            prev = cur
            cur = nxt
        l1,l2=head,prev
        while l2.next:
            l1Nxt, l2Nxt = l1.next, l2.next
            l1.next = l2
            l2.next = l1Nxt
            l1, l2 = l1Nxt, l2Nxt