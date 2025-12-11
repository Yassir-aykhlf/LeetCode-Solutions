# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            fast =fast.next.next
            slow =slow.next
        prev = None
        mid = slow
        while mid:
            midNxt = mid.next
            mid.next = prev
            prev = mid
            mid = midNxt
        l, r = head, prev
        while r.next:
            l_next, r_next = l.next, r.next
            l.next = r
            r.next = l_next
            l, r = l_next, r_next