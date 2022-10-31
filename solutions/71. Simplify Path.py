class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split('/')
        s = []
        for dir in dirs:
            if not dir or dir == "." or dir == "..":
                if s and dir == "..":
                    s.pop()
            else:
                s.append(dir)
        res = ""
        for dir in s:
            res += "/" + dir
        return res if s else "/"
