# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
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
        while r2:
            if r1.val != r2.val:
                return False
            r2 = r2.next
            r1 = r1.next
        return True