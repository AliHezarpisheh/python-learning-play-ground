"""
933. Number of Recent Calls

Topics: `queues`, `data stream`.

My first instinct was to store all the numbers in the `items`, and then use sum() with
a list comprehension to count the numbers that are within the valid range.

```python
from collections import deque

class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        valid_range = range(t - 3000, t)
        return sum(
            1
            number for number in self.queue
            if number in valid_range
        )
```

But this is inefficient. Every time you're checking the numbers that you previously
could determine that they are not valid anymore. So, the final solution use an approach
that removes the numbers that are not needed anymore. Also, the `len` in Python has O(1)
time complexity, because in RAM, lists are stored as tables (series of contiguous
addresses), and to know the length of the list, so for RAM to know that where the list
ends, it should know the start address and the **length** of the list, so the length
is stored.

https://leetcode.com/problems/number-of-recent-calls/description/?envType=problem-list-v2&envId=queue
"""

from collections import deque


class RecentCounter:
    def __init__(self):
        self.items = deque()

    def ping(self, t: int) -> int:
        self.items.append(t)

        while self.items[0] < t - 3000:
            self.items.popleft()
        return len(self.items)


if __name__ == "__main__":
    counter = RecentCounter()
    print(counter.ping(1))
    print(counter.ping(100))
    print(counter.ping(3001))
    print(counter.ping(3002))
