# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        mid = slow
        prev = None
        while mid:
            midNext = mid.next
            mid.next = prev
            prev = mid
            mid = midNext
        r1, r2 = head, prev
        while r2.next:
            r1Next, r2Next = r1.next, r2.next
            r1.next = r2
            r2.next = r1Next
            r1, r2 = r1Next, r2Next