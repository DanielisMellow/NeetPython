class Solution:

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        results = []
        for i in range(len(nums)):

            left = nums[0:i]
            right = nums[i + 1 : len(nums)]
            joined_List = left + right
            product = 1
            for number in joined_List:
                product *= number
            results.append(product)

        return results

    def productExceptSelfV2(self, nums: list[int]) -> list[int]:
        result = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        print(result)

        postfix = 1
        for j in range(len(nums) - 1, -1, -1):
            result[j] *= postfix
            postfix *= nums[j]

        return result


def main():

    nums = [
        1,
        2,
        3,
        4,
    ]
    nums2 = [-1, 1, 0, -3, 3]

    num_lists = [nums, nums2]
    s = Solution()

    for test in num_lists:

        print(f"Testing List:{test}")
        print(f"Result:{s.productExceptSelfV2(test)}")
        print("\n\n")


if __name__ == "__main__":
    main()
