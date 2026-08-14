"""
71. Simplify Path

Topics: `stack`, `string`.

https://leetcode.com/problems/simplify-path/description/?envType=problem-list-v2&envId=stack
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        SLASH = "/"
        IGNORE_TOKENS = {"", "."}
        PREVIOUS_DIR = ".."

        tokens = path.split(SLASH)
        stack = []
        for token in tokens:
            if token in IGNORE_TOKENS:
                continue
            elif token == PREVIOUS_DIR:
                if stack:
                    stack.pop()
            else:
                stack.append(token)

        return SLASH + SLASH.join(stack)


if __name__ == "__main__":
    path = input("Path: ")
    print(Solution().simplifyPath(path=path))
