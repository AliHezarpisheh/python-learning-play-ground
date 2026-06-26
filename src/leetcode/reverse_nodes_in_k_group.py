class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        previous: ListNode | None = None
        current = head
        while current:
            last_node = current
            for _ in range(k):
                old_next = current.next
                current.next = previous

                previous = current
                current = old_next
            previous = old_next
            current = old_next.next
            last_node.next = old_next

        new_head = head
        for _ in range(k):
            new_head = head.next
        return new_head


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
    k = int(input("k: "))

    print(Solution().reverseKGroup(head=head, k=k))
