class Solution:
    def isPalindrome(self, s: str) -> bool:
        lis = [ch.lower() for ch in s if ch.isalnum()]

        for i in range(int(len(lis) / 2)):
            if lis[i] != lis[-(i + 1)]:
                return False
        return True