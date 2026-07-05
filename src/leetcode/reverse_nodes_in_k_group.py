class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"{self.val}"

    def __repr__(self) -> str:
        return f"{self.val}"


# Recursive approach
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        if head is None:
            return None

        tail = head
        for _ in range(k):
            if tail is None:
                return head
            tail = tail.next

        def reverse_nodes(current: ListNode | None, end: ListNode) -> ListNode:
            previous = None

            while current != end:
                old_next = current.next
                current.next = previous
                previous = current
                current = old_next

            return previous

        new_head = reverse_nodes(current=head, end=tail)
        head.next = self.reverseKGroup(head=tail, k=k)

        return new_head


# Iterative approach
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        dummy = ListNode(0, head)
        group_previous = dummy

        def get_kth_node(start: ListNode, k: int) -> ListNode:
            while start and k > 0:
                start = start.next
                k -= 1
            return start

        while True:
            kth_node = get_kth_node(start=group_previous, k=k)
            if not kth_node:
                break
            group_next = kth_node.next

            previous, current = group_next, group_previous.next
            while current != group_next:
                tmp = current.next
                current.next = previous
                previous = current
                current = tmp
            new_group_previous = group_previous.next
            group_previous.next = previous
            group_previous = new_group_previous
        return dummy.next


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

    new_head = Solution().reverseKGroup(head=head, k=k)
    print(new_head)
    while new_head.next:
        new_head = new_head.next
        print(new_head)
