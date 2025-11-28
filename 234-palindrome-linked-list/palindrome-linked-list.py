# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
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
        while r2:
            if r1.val != r2.val:
                return False
            r1 = r1.next
            r2 = r2.next
        return True