class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid_string=("".join([a for a in s if a.isalnum()])).lower()
        r=len(valid_string)-1;
        for l in valid_string:
            if l==valid_string[r]:
                r-=1
            else:
                return False

        return True

