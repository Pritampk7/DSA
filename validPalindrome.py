class ValidPalindrome:

    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            while not self.checkalpha(s[left]):
                left += 1

            while not self.checkalpha(s[right]):
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left, right = left+1, right-1

        return True

    def checkalpha(self, char):
        return ord(char) in range(ord('A'), ord('Z')) or \
               ord(char) in range(ord('a'), ord('z')) or \
               ord(char) in range(ord('0'), ord('9'))


obj = ValidPalindrome()
print(obj.isPalindrome("A man, a plan, a canal: Panama"))
