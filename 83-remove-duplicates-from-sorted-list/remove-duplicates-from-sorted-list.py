# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        curr = head
        while curr:
            nums.append(curr.val)
            curr = curr.next
        nums_ = sorted(list(set(nums)))
        dummy = ListNode(-1)
        curr = dummy
        for n in nums_:
            curr.next = ListNode(n, None)
            curr = curr.next
        return dummy.next