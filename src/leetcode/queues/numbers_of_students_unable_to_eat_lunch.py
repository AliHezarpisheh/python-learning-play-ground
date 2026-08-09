"""
1700. Number of Students Unable to Eat Lunch

Topics: `queues`, `array`, `stack`, `simulation`.

The first solution is the naive one I came up with. The last part of it is super
inefficient, but the rest is not bad, sticking to simulation. The second one is more
optimized one, without simulation. It actually uses a really tricky mathematical
solution that introduces O(n) time complexity and O(1) auxiliary space complexity.

https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/description/?envType=problem-list-v2&envId=queue
"""

import numpy
from collections import deque


class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        students: deque[int] = deque(students)
        sandwiches: deque[int] = deque(sandwiches)

        while sandwiches:
            student_choice = students.popleft()
            if student_choice == sandwiches[0]:
                sandwiches.popleft()
            else:
                students.append(student_choice)

            if len(students) == 0:
                return 0

            count_1 = numpy.sum(students)
            if (len(students) == count_1 or count_1 == 0) and students[0] != sandwiches[
                0
            ]:
                return len(students)


class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        counts = [0, 0]

        for student in students:
            counts[student] += 1

        for sandwich in sandwiches:
            if counts[sandwich] == 0:
                return sum(counts)
            counts[sandwich] -= 1
        return 0


if __name__ == "__main__":
    students = [int(student) for student in input("student: ").split()]
    sandwiches = [int(sandwich) for sandwich in input("sandwiches: ").split()]
    print(Solution().countStudents(students=students, sandwiches=sandwiches))
