class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split('/')
        stack = []
        for dir_ in dirs:
            if dir_ == '..':
                if stack:
                    stack.pop()
            elif dir_ and dir_ != '.':
                stack.append(dir_)
        return '/' + '/'.join(stack)