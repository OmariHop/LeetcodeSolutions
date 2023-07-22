class Solution(object):
    def topKFrequent(self, nums, k):
        # Hashmap for getting the values as well as their frequency, list is for the output 
        myHash = {}
        mylist = []
        greatestFreq = 0
        # Adding the number to the hasmap if it is not found while setting their frequency to q 
        # If it is found, we update the frequency 
        for num in nums:
            if num not in myHash:
                myHash[num] = 1

            else:
                myHash[num]+= 1
        # For loop that runs K times, checks to see the first max key, value pair in the map, appends its key to the list, and pops it
        for i in range(k):
            greatestFreq = max(myHash, key=myHash.get)
            mylist.append(greatestFreq)
            myHash.pop(greatestFreq)

        return mylist
            
