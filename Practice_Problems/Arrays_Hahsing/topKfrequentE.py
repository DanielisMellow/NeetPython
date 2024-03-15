from collections import Counter
from heapq import heapify, heappop, heappush


class Solution:
    # kLogn soulution with O(n) space
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        countNums = dict()

        ## increment occurence of an item
        for num in nums:
            countNums[num] = countNums.get(num, 0) + 1

        ## Dictionary comprehension flip key and value pairs
        countNums_inv = {v: k for k, v in countNums.items()}
        ## List of new keys but negative to use min heap
        h = [i * -1 for i in countNums_inv.keys()]
        print(h)
        print(countNums_inv)
        heapify(h)

        ## return a list of top k elements
        return [countNums_inv[abs(heappop(h))] for i in range(k)]

    # O(n) time complexity
    def topKFrequentV2(self, nums: list[int], k: int) -> list[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            freq[c].append(n)
        print(freq)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


def main():

    nums = [1, 1, 1, 2, 2, 3]
    print(nums)
    k = 1
    S = Solution()
    print(S.topKFrequentV2(nums, k))


if __name__ == "__main__":
    main()
