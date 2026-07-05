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
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        result = []
        if root:
            result = self.inorderTraversal(root.left)
            result.append(root.val)
            result += self.inorderTraversal(root.right)
        return result


class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        if root:
            self.inorderTraversal(root=root.left)
            print(root.val)
            self.inorderTraversal(root=root.right)


from collections.abc import Generator


class Solution:
    def inorder_traverse(self, root: TreeNode | None) -> list[int]:
        result = []
        for val in self._inorder_traverse(root=root):
            result.append(val)
        return result

    def _inorder_traverse(self, root: TreeNode | None) -> Generator[int]:
        if root is None:
            return None

        yield from self._inorder_traverse(root.left)
        yield root.val
        yield from self._inorder_traverse(root.right)


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

    print(Solution().inorderTraversal(root=root))
