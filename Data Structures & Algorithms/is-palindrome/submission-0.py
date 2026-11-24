class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome=''
        for char in s:
            if char.isalnum():
                palindrome+=char.lower()
        return palindrome==palindrome[::-1]        
        