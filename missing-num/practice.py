'''Given an array arr[] of size n-1 with distinct integers in the range of [1, n]. This array represents a permutation of the integers from 1 to n with one element missing. Find the missing element in the array.

Examples: 

Input: arr[] = [8, 2, 4, 5, 3, 7, 1]
Output: 6
Explanation: All the numbers from 1 to 8 are present except 6.

Input: arr[] = [1, 2, 3, 5]
Output: 4
Explanation: Here the size of the array is 4, so the range will be [1, 5]. The missing number between 1 to 5 is 4
'''
# my solution time - O(n) space - O(1)
def findMissingNum(arr):
    max_num = max(arr) + 1

    for i in range (1,max_num):
        if i not in arr:
            return i
        
    return -1

arr = [8, 2, 4, 5, 3, 7, 1]
print(findMissingNum(arr))

# nartive approch linear search for missing number time complexity O(n)^2 space complexity O(1)

def searchTheMissingNumber(arr):
    n = len(arr) + 1

    for i in range(1,n+1):
        found = False
        for j in range(n-1):
            if i == arr[j]:
                found = True
                break
        if not found:
            return i
    return -1

print(searchTheMissingNumber(arr))

def missingNum(arr):
    n = len(n) + 1

    hash = [0] *(n+1) 


                
def findTheLostNum(arr):
    n = len(arr) + 1

    # create a hash array of size i more than 
    hash = [0] * (n+1)

    # itrate to store frequancy array
    for i in range(n-1):
        hash[arr[i]] +=1

    # itrate the frequancy to find the missing num

    for i in range(1, n+1):
        if hash[i] == 0:
            return i
    return -1

print(findTheLostNum(arr))

# matimaical method the sum of n terms time - O(n) and space O(1)

def findTheMissing(arr):
    n = len(arr) + 1
    sum = (n*(n+1)) // 2
    total = 0

    for i in range(n-1):
        total += arr[i]

    return sum - total

print(findTheMissing(arr))

# using XOR opration

def findTheMissing2(arr):
    n = len(arr) + 1

    xor1 = 0
    xor2 = 0

    for i in range(n-1):
        xor1 ^= arr[i]

    for i in range(1,n+1):
        xor2 ^= i

    return xor1 ^ xor2

print(findTheMissing2(arr))