"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_to_clone = {None: None}
        curr = head
        while curr:
            clone = Node(curr.val)
            node_to_clone[curr] = clone
            curr = curr.next
        curr = head
        while curr:
            clone = node_to_clone[curr]
            clone.next = node_to_clone[curr.next]
            clone.random = node_to_clone[curr.random]
            curr = curr.next
        return node_to_clone[head]