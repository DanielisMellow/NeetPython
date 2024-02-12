# 217. Contatins Duplicates
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashSet = set()

        for i in nums:
            if i in hashSet:
                return True
            hashSet.add(i)
        return False


def main():

    numbers = [1, 2, 3, 4]

    S = Solution()

    print(S.containsDuplicate(numbers))


if __name__ == "__main__":
    main()
