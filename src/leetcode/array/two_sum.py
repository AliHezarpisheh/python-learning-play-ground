"""
1. Two Sum

Topics: `array`.

Yeah, there is not much to say. The second approach has O(n) time complexity.

https://leetcode.com/problems/two-sum/solutions/3619262/3-methods-c-java-python-beginner-friendl-x595/
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for index_1 in range(len(nums)):
            for index_2 in range(index_1 + 1, len(nums)):
                if nums[index_1] + nums[index_2] == target:
                    return [index_1, index_2]
        return []


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_map: dict[int, int] = {number: index for index, number in enumerate(nums)}

        for index, num in enumerate(nums):
            compliment = target - num
            if compliment in num_map and index != num_map[compliment]:
                return [index, num_map[compliment]]
        return []


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_map: dict[int, int] = {}

        for index, num in enumerate(nums):
            compliment = target - num
            if compliment in num_map and index != num_map[compliment]:
                return [index, num_map[compliment]]
            num_map[num] = index
        return []
