# 125. Valid Palindrome
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.


class Solution:
    def isPalindrome(self, s: str) -> bool:

        alphaS = ""
        for c in s:
            if c.isalnum():
                alphaS += c.lower()

        reversedStr = alphaS[::-1]

        print(alphaS)
        print(reversedStr)

        if alphaS == reversedStr:
            return True

        return False

    def isAlphaNum(self, s: str) -> bool:
        if (
            ord("A") <= ord(s) <= ord("Z")
            or ord("a") <= ord(s) <= ord("z")
            or ord("0") <= ord(s) <= ord("9")
        ):
            return True
        return False

    def isPalindromeV2(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i < j:

            while i < j and not self.isAlphaNum(s[i]):
                i += 1
            while j > i and not self.isAlphaNum(s[j]):
                j -= 1

            if s[i].lower() != s[j].lower():
                return False
            i, j = i + 1, j - 1

        return True


def main():

    str = "A man, a plan, a canal: Panama"
    S = Solution()
    print(S.isPalindromeV2(str))


if __name__ == "__main__":
    main()
