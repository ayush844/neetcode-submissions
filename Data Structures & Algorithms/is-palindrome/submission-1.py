class Solution:
    def isPalindrome(self, s: str) -> bool:
        text_arr = [text.lower() for text in s if text.isalnum()]
        l = 0
        r = len(text_arr)-1

        while l < r:
            if text_arr[l] != text_arr[r]:
                return False
            l+=1
            r-=1

        return True