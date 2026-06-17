class Codec:
    def serialize(self, root):
        res = []
        def dfs(node):
            if not node:
                res.append('N')
                return
            res.append(str(node.val)) 
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ','.join(res)

    def deserialize(self, data):
        data_ = data.split(',')[::-1]
        def build():
            val = data_.pop()
            if val == 'N':
                return None
            node = TreeNode(int(val))
            node.left =  build()
            node.right = build()
            return node
        return build()