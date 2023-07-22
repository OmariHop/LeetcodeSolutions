class Solution(object):


    # Prime numbers that help us with representation of letters with combinations of unique values due to prime facotorization
    # Because we are dealing with prime numbers, we are able to encounter a duplicate Hash value a different combination of numbers. (No two different combinations of prime numbers mulitply to the same product)

    prime_nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101] 

    def groupAnagrams(self, strs):

        # HashMap that is used to hold the hash value and the words that would share the same hash
        myHash = {}
        output = []


# Iterating through each string in our array, calculating a hash value based on their product of primes, and seeing if it is contained within the hash map. 
# If it is, the string is added as a value to the prexisting word, else we just add the hash value as a new key along with the value 
        for word in strs:
            hashVal = self.hashFunc(word)
            if hashVal in myHash:
                myHash[hashVal].append(word)
            else:
                myHash[hashVal] = [word]

        # making thhe hash a list based on their values
        output = list(myHash.values())

        return output
       




    def hashFunc(self, word):


        hashVal = 1
        for char in word:
            # Calculating the hash value of a word using the index of our primes
            hashVal = hashVal  * self.prime_nums[ord(char) - ord('a')]


        return hashVal

        
