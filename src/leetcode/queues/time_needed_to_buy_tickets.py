"""
2073. Time Needed to Buy Tickets

Topics: `array`, `queue`, `simulation`.

The first solution, was my first instinct, after reading about `simulation`. But I don't
like the code I wrote. The time complexity is O(i∑​tickets[i])? and the space complexity
is O(n). I saw the second solution in leetcode solutions and I thought it was very
clever. The time complexity is O(n) and the space complexity is O(1). The third solution
is still a simulation with same complexities, but it is a better and cleaner approach
compared to the first simulation.

https://leetcode.com/problems/time-needed-to-buy-tickets/description/?envType=problem-list-v2&envId=queue
"""


from collections import deque


class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        queue: deque[int] = deque(tickets)
        len_queue = len(queue)

        counter = 0
        while queue:
            ticket = queue.popleft()
            ticket -= 1
            if ticket != 0:
                queue.append(ticket)
                k = (k - 1) % len_queue
            else:
                if k == 0:
                    return counter + 1
                len_queue -= 1
                k -= 1
            counter += 1


class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        result = 0

        for index, value in enumerate(tickets):
            if index <= k:
                result += min(value, tickets[k])
            else:
                result += min(value, tickets[k] - 1)
        return result


class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        queue: deque[tuple[int, int]] = deque(enumerate(tickets))
        counter = 0

        while queue:
            person, remaining_tickets = queue.popleft()

            remaining_tickets -= 1

            if remaining_tickets == 0:
                if person == k:
                    return counter + 1
            else:
                queue.append((person, remaining_tickets))

            counter += 1


if __name__ == "__main__":
    tickets = [int(ticket) for ticket in input("tickets: ").split()]
    k = int(input("k: "))
    print(Solution().timeRequiredToBuy(tickets=tickets, k=k))
