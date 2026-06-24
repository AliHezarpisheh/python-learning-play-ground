class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"{self.val}"

    def __repr__(self) -> str:
        return f"{self.val}"


class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return

        very_previous_node: ListNode | None = None
        previous_node = head
        current_node = head.next
        while previous_node.next:
            previous_node.next = current_node.next
            current_node.next = previous_node
            if very_previous_node:
                very_previous_node.next = current_node

            # Change the head if necessary.
            if previous_node is head:
                head = current_node

            # Update nodes.
            if previous_node.next is None:
                break
            current_node = previous_node.next.next
            very_previous_node = previous_node
            previous_node = previous_node.next
        return head


if __name__ == "__main__":
    head: ListNode | None = None
    for text in input("Numbers: ").split():
        num = int(text)  # Assuming user won't enter random shit.
        node = ListNode(val=num)
        if not head:
            head = node
        else:
            previous_node.next = node
        previous_node = node

    head = Solution().swapPairs(head=head)

    while head:
        data = head.val
        print(data)
        head = head.next
