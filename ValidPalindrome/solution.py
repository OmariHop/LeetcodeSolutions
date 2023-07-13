    def isPalindrome(self, s):
        if s == " ":
            return True

        l = 0
        r = len(s) - 1

        while l< r:
            while l< r and not s[l].isalnum():
                l = l + 1
            while r > l and not s[r].isalnum():
                r = r - 1 

            if s[l].lower() == s[r].lower():
                l = l + 1
                r = r - 1
                continue
            else:
                return False

        return True
