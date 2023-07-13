class Solution(object):
    def twoSum(self, nums, target):
        myDict = {}
        ret = []

        for i, num in enumerate(nums):
            if num not in myDict:
                myDict[num] = i

        for i, num in enumerate(nums):
            complement = target - num
            if complement in myDict and myDict[complement] != i:
                ret = [i, myDict[complement]]
                break

        return ret
