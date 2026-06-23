class Solution:
    def simplifyPath(self, path: str) -> str:
        chunks = path.split('/')
        stack  = []
        for chunk in chunks:
            if stack and chunk == '..':
                stack.pop()
            elif chunk and chunk != '.' and chunk != '..':
                stack.append(chunk)
        return '/' + '/'.join(stack)