class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        left = 1
        for right in range(1, len(nums)):
            if nums[right] > nums[right - 1]:
                nums[left] = nums[right]
                left += 1
        return left, nums


def main():
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(nums)
    S = Solution()
    print(S.removeDuplicates(nums))


if __name__ == "__main__":
    main()
