'''Given an integer array arr[], compute the sum of all possible sub-arrays of the array. A sub-array is a contiguous part of the array.

Examples: 

Input: arr[] = [1, 4, 5, 3, 2]
Output: 116
Explanation: Sum of all possible subarrays of the array [1, 4, 5, 3, 2] is 116.

Input: arr[] = [1, 2, 3, 4]
Output: 50
Explanation: Sum of all possible subarrays of the array [1, 2, 3, 4] is 50.'''

# Native Approch
# time complexity O(n)^2 and space complexity O(n)

def sumAllArr(arr):

    n = len(arr)
    result = 0

    for i in range(n):
        temp = 0
        
        for j in range(i,n):
            temp += arr[j]
            result += temp

    return result

if __name__ == "__main__":
    arr = [1, 4, 5, 3, 2,8]
    print(sumAllArr(arr))