"""
114. Flatten Binary Tree to Linked List

Topics: `trees`, `linked-list`, `binary trees`, `stack`, `depth-first search`.

https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/?envType=problem-list-v2&envId=stack
"""

# TODO: Solve using Morris Traversal

from collections.abc import Iterator


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.val)


class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        numbers = list(self._preorder_traverse(node=root))

        for number in numbers[1:]:
            root.right.val = number
            root.left = None
            root = root.right

    @staticmethod
    def _preorder_traverse(node: TreeNode | None) -> Iterator[int]:
        if node is None:
            return

        yield node.val
        yield from Solution._preorder_traverse(node=node.left)
        yield from Solution._preorder_traverse(node=node.right)


if __name__ == "__main__":
    A = TreeNode(1)
    B = TreeNode(2)
    C = TreeNode(3)
    D = TreeNode(4)
    E = TreeNode(5)
    F = TreeNode(6)
    G = TreeNode(7)
    H = TreeNode(8)

    A.left = B
    A.right = C
    B.left = D
    B.right = E
    D.left = G
    D.right = H
    A.right = C
    C.right = F

    # This is what the above tree would look like:
    #        1
    #       / \
    #      2  3
    #     / \  \
    #    4  5  6
    #   / \
    #  7  8

    root = Solution().flatten(root=A)
