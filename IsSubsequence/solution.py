class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

      # Empty S string case
        if s == "":
            return True
          # Empty T string case
        if t == "":
            return False


        # Setting pointers for both strings to 0 for iteration
        tPointer = 0
        sPointer = 0

      # Grabbing the length of both strings for comparsion of pointers
        tLength = len(t)
        sLength = len(s)
        


        for i in range(tLength):
          # matching letter case
            if t[tPointer] == s[sPointer]:
                tPointer = tPointer + 1
                sPointer = sPointer + 1
              # letters do not match, but we still increment t's pointer
            else:
                tPointer = tPointer + 1

          # conditions to check if there is some indication of there being a matching substring or not
            if tPointer > tLength - 1 and sPointer> sLength - 1:
                return True
            if sPointer > sLength - 1:
                return True
            if tPointer > tLength - 1:
                return False
        

        return False
