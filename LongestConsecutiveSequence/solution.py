class Solution(object):
    def longestConsecutive(self, nums):
        # Creating a set that holds our array for look ups 
        mySet = set() 
        # Best and curr are used to compare the number of sequences we encounter in our set
        # A start of sequence is defined as a number that does not have a preceeding number before it 
        # OR n - 1
        currSeq = 0
        bestSeq = 0

        # Adding numbers to our set
        # Could have used mySet = set(nums)

        for num in nums:
            mySet.add(num)


# Iterating through set to check for n-1 number for each element in the set, if we find an element we skip
# Runtime is O(n + m) where m is the max length of a sequence
# The sequence can only be up untill N
        for num in mySet:
            j = 1
            currSeq = 1
            if num - 1 in mySet:
                continue
            else:
                while num + j in mySet:
                    currSeq = currSeq + 1
                    j = j + 1             
            # Gets the max between our current sequence and the best                  
            bestSeq = max(bestSeq, currSeq) 

# Returns the best sequence 
        return bestSeq
