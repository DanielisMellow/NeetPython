# 242. Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sSorted = "".join(sorted(s))
        tSorted = "".join(sorted(t))

        print(f"s:{sSorted} t:{tSorted}")

        return sSorted == tSorted

    def isAnagramV2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i, (sChar, tChar) in enumerate(zip(s, t)):
            countS[sChar] = countS.get(sChar, 0) + 1
            countT[tChar] = countT.get(tChar, 0) + 1
        print(f"{countS}\n{countT}")

        for key in countS:
            if countS[key] != countT.get(key, 0):
                return False

        return True

    def isAnagramV3(self, s: str, t: str) -> bool:
        print(f"{Counter(s)}\n{Counter(t)}")
        return Counter(s) == Counter(t)


def main():
    s = "anagram"
    t = "nagaram"

    S = Solution()
    # V2 is the preferred one in an interview
    print(S.isAnagramV3(s, t))


if __name__ == "__main__":
    main()
