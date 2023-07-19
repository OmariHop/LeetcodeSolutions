class Solution(object):
    def maxProfit(self, prices):


        arrLen = len(prices)    ## Gets the length of the array to control our loop 
        bestPrice = 0       # Keeps track of the best price for comparision between two intervals


# Base case that returns 0 if the length of the array is 1, meaning that there is no best time to buy a stock
        if arrLen == 1: 
            return bestPrice 
        l = 0   
        r = 1 

        # Loop that is controlled up untill our right pointer is exceeds the indices of the array 
        while r != arrLen: 
            # If we find a case where l is greater than right, we can limit our search untill we find something that is less
            # We know that anything > r up untill r is greater than l has a greater difference so we can just contunue to move up
            if prices[l] > prices[r]:
                l = r
                r = r + 1
                # Once we hit a value that is greater, we can compare the difference of the previous max and the current difference, we return the max of the two
            elif prices[l] < prices[r]:
                currPrice = prices[r] - prices[l]
                if currPrice > bestPrice:
                    bestPrice = currPrice 
                r = r + 1
                # Handles duplicate values, in which we continue searching
            else:
                r = r + 1


        return bestPrice
