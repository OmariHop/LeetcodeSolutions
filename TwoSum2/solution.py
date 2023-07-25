class Solution(object):
    def twoSum(self, numbers, target):

        # Output array to hold our indices 
        output = []

        # Setting the left and right pointers to the beginning and the end of our sorted array to set of the two pointer method approach 
        l = 0
        r = len(numbers) - 1
        # loops untill l equals r, condition really isnt needed since we are gaurenteed a solution
        while l != r:
            # Decreasing our search if our sum is greater than the target
            if numbers[l] + numbers[r] > target:
                r = r - 1
            # Increasing the scope of our search if the sum is less than the target
            elif numbers[l] + numbers[r] < target:
                l = l + 1
            # When we have found our target, we increament the indicies by 1 and then append them to our list
            else:
                l+=1
                r+=1
                output.append(l)
                output.append(r)
                return output



        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
