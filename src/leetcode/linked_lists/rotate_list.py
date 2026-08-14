"""
61. Rotate List

Topics: `linked-list`, `two-pointers`.

The first solution was the first thing that came into my mind. The issue of it was that
a large number k could make a lot of overhead. In the second approach, I add a O(n)
iteration on the list, to calculate the length of the list, so I could find the optimal
k. If this was a real application code, I would calculate the items of the list at first
or when the list is getting build, and then pass it to the function. The third solution
uses a very good trick, by handling the edge cases, optimize k, making the list circular
and finding the tail of the rotated list with one iteration.

https://leetcode.com/problems/rotate-list/description/?envType=problem-list-v2&envId=linked-list
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if head is None:
            return None
        if head.next is None:
            return head

        for _ in range(k):
            previous: ListNode | None = None
            current: ListNode = head
            while current.next is not None:
                previous = current
                current = current.next

            previous.next = None
            current.next = head
            head = current
        return head


class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if head is None:
            return None
        if head.next is None:
            return head

        list_length = 0
        current = head
        while current:
            list_length += 1
            current = current.next

        k = k % list_length
        for _ in range(k):
            previous: ListNode | None = None
            current: ListNode = head
            while current.next is not None:
                previous = current
                current = current.next

            previous.next = None
            current.next = head
            head = current
        return head


class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if head is None or head.next is None or k == 0:
            return head

        list_length = 1
        tail = head
        while tail.next:
            list_length += 1
            tail = tail.next

        k %= list_length
        if k == 0:
            return None

        tail.next = head

        new_tail = head
        for _ in range(list_length - k - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None
        return new_head
