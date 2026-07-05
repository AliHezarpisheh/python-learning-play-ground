from collections.abc import Generator


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        print(root.data)


class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        result = []
        for val in self._postorderTraversal(root=root):
            result.append(val)
        return result

    def _postorderTraversal(self, root: TreeNode | None) -> Generator[int]:
        if root is None:
            return None

        yield from self._postorderTraversal(root=root.left)
        yield from self._postorderTraversal(root=root.right)
        yield root.val


class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        result = []
        if root:
            result += self.postorderTraversal(root=root.left)
            result += self.postorderTraversal(root=root.right)
            result.append(root.val)
        return result


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

    print(Solution().postorderTraversal(root=root))
