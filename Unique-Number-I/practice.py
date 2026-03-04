'''Given an array of integers, every element in the array appears twice except for one element which appears only once. The task is to identify and return the element that occurs only once.

Examples: 

Input:  arr[] = [2, 3, 5, 4, 5, 3, 4]
Output: 2 
Explanation: Since 2 occurs once, while other numbers occur twice, 2 is the answer.

Input: arr[] = [2, 2, 5, 5, 20, 30, 30]
Output: 20
Explanation: Since 20 occurs once, while other numbers occur twice, 20 is the answer.'''

# narive approch or brute force time complexity O(n)^2 space complexity O(1)

def returnUnique(arr):

    unique = []

    n = len(arr)
    for i in range(n):
        count = 0

        for j in range(n):
            if arr[i] == arr[j]:
                count += 1
            
        if count == 1:
            return arr[i]
    return -1
    

# the hash map approch

def findUnique(arr):
    dir = {}

    for num in arr:
        dir[num] = dir.get(num,0) + 1
    
    for key, value in dir.items():
        if value == 1:
            return key
        
    return -1


# XOR opration time complexity O(n) and space complexity O(1)

def findSingle(arr):
    res = 0

    for num in arr:
        res ^= num
    
    return res


if __name__ == "__main__":
    arr = [2,2,1, 3, 5, 4, 5, 3, 4]
    print("First Approch")
    print(returnUnique(arr))
    print("Second Approch")
    print(findUnique(arr))
    print("Third approch")
    print(findSingle(arr))
