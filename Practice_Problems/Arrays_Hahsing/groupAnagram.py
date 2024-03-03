# 49. Group Anagrams
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagramDict = dict()

        for word in strs:
            anagramDict.setdefault("".join(sorted(word)), []).append(word)

        print(anagramDict)
        return list(anagramDict.values())


def main():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

    S = Solution()

    print(S.groupAnagrams(strs))


if __name__ == "__main__":
    main()
