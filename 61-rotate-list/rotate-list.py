# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        k = k % len(arr)
        rev = list(reversed(list(reversed(arr[:-k])) + list(reversed(arr[-k:]))))
        dummy = ListNode(-1)
        curr = dummy
        for num in rev:
            curr.next = ListNode(num)
            curr = curr.next
        return dummy.next