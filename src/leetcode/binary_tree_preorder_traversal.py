# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"{self.val}"

    def __repr__(self) -> str:
        return f"{self.val}"


class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        if root:
            print(root.val)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)


class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        result = []
        if root:
            result.append(root.val)
            result += self.preorderTraversal(root=root.left)
            result += self.preorderTraversal(root=root.right)
        return result


from collections.abc import Generator


class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        result = []
        for val in self._preorderTraversal(root=root):
            result.append(val)
        return result

    def _preorderTraversal(self, root: TreeNode | None) -> Generator[int]:
        if root is None:
            return None

        yield root.val
        yield from self._preorderTraversal(root=root.left)
        yield from self._preorderTraversal(root=root.right)


if __name__ == "__main__":
    numbers = [int(num) for num in input("Numbers: ").split()]
    len_numbers = len(numbers)
    root = TreeNode(val=numbers[0])

    from collections import deque

    index = 1
    current = root
    queue: deque[TreeNode] = deque()
    queue.append(root)
    while queue:
        node: TreeNode = queue.popleft()
        if numbers[index] and index % 2 == 1:
            new_node = TreeNode(val=numbers[index])
            node.left = new_node
            queue.append(new_node)
            index += 1
            if index >= len_numbers:
                break
        if numbers[index] and index % 2 == 0:
            new_node = TreeNode(val=numbers[index])
            node.right = new_node
            queue.append(new_node)
            index += 1
            if index >= len_numbers:
                break

    print(Solution().preorderTraversal(root=root))
