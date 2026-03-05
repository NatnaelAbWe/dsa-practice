'''Given an array arr[] of size n filled with numbers from 1 to n-1 in random order. The array has only one repetitive element. The task is to find the repetitive element.

Examples:

Input: arr[] = [1, 3, 2, 3, 4]
Output: 3
Explanation: The number 3 is the only repeating element.

Input: arr[] = [1, 5, 1, 2, 3, 4]
Output: 1
Explanation: The number 1 is the only repeating element.

'''

# native approch 

def search_duplicate(arr):
    n = len(arr)

    for i in range(n):
        for j in range(i+1,n):
            if arr[i] == arr[j]:
                return arr[i]
    return -1
    
if __name__ == "__main__":
    arr = [1, 3, 2, 3, 4]
    print(search_duplicate(arr))

# [Better Approach 1] Sorting - O(n Log n) Time and O(1) Space

def find_duplicate(arr):
    arr.sort()

    for i in range(len(arr)):
        if arr[i] == arr[i+1]:
            return arr[i]
    return -1

find_duplicate(arr)