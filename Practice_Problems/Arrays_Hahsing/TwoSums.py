# 1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        idxs = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                print(f"i:{i} j:{j}\n{nums[i]}+{nums[j]}={nums[i]+nums[j]}")
                if nums[i] + nums[j] == target:
                    idxs.append(i)
                    idxs.append(j)
                    return idxs
        return idxs

    def twoSumV2(self, nums: list[int], target: int) -> list[int]:
        prevMap = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in prevMap:
                return [prevMap[diff], i]
            print(prevMap)
            prevMap.update({num: i})
        return []


def main():

    numbers = [15, 2, 11, 7]
    target = 9

    S = Solution()

    print(S.twoSum(numbers, target))
    print()
    print(S.twoSumV2(numbers, target))


if __name__ == "__main__":
    main()
