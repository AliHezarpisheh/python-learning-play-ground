"""
387. First Unique Character String

Topics: `hash table`, `string`, `queue`.

Simple question, nothing especial. The second solution is using unicode numbers as
indexes of an array/list, to keep track of the character counts, instead of a
dictionary. The second solution doesn't give us any efficiency in time and space, but
it was fun so I included it.

https://leetcode.com/problems/first-unique-character-in-a-string/description/?envType=problem-list-v2&envId=queue
"""

from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        character_counter = Counter(s)
        for index, character in enumerate(s):
            if character_counter[character] == 1:
                return index
        return -1


class Solution:
    def firstUniqChar(self, s: str) -> int:
        character_counts = [0] * 26
        ord_a = ord("a")  # Unicode number of `a` -> 97.
        for character in s:
            unicode_number = ord(character)
            character_counts[unicode_number - ord_a] += 1

        for index, character in enumerate(s):
            if character_counts[ord(character) - ord_a] == 1:
                return index

        return -1


if __name__ == "__main__":
    value = input("Enter the value: ")
