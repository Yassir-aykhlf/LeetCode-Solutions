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
        cur_copy = {None : None}
        cur = head
        while cur:
            node = Node(cur.val)
            cur_copy[cur] = node
            cur = cur.next
        cur = head
        while cur:
            node = cur_copy[cur]
            node.next = cur_copy[cur.next]
            node.random = cur_copy[cur.random]
            cur = cur.next
        return cur_copy[head]