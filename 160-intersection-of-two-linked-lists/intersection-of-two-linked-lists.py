# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        rA, rB = headA, headB
        while rA != rB:
            rA = rA.next if rA is not None else headB
            rB = rB.next if rB is not None else headA
        return rA