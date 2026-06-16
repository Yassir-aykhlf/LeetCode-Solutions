# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        if not root: return 'N'
        res = []
        def preorder(node):
            if not node:
                res.append('N')
                return
            res.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return ','.join(res)

    def deserialize(self, data):
        data_ = data.split(',')[::-1]
        def build():
            val = data_.pop()
            if val == 'N':
                return None
            node = TreeNode(int(val))
            node.left = build()
            node.right = build()
            return node
        return build()