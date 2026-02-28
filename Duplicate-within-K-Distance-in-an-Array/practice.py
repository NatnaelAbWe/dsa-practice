'''
Given an integer array arr[] and an integer k, determine whether there exist two indices i and j such that arr[i] == arr[j] and |i - j| ≤ k. If such a pair exists, return 'Yes', otherwise return 'No'.

Examples: 

Input: k = 3, arr[] = [1, 2, 3, 4, 1, 2, 3, 4]
Output: No
Explanation: Each element in the given array arr[] appears twice and the distance between every element and its duplicate is 4.

Input: k = 3, arr[] = [1, 2, 3, 1, 4, 5]
Output: Yes
Explanation: 1 is present at index 0 and 3.

Input: k = 3, arr[] = [1, 2, 3, 4, 5]
Output: No
Explanation: There is no duplicate element in arr[].
'''

# native of the bruteforce approch
# with O(n)^2 time complexity and O(n) space complexity

def check_duplicate_within_k(arr,k):
    
    fin = len(arr)
    for i in range(0,fin):
      for j  in range(i+1,fin):
         if arr[i] == arr[j] and abs(i-j) <= k:
            return True;
    return False


arr = [10, 5, 3, 4, 3, 5, 6]
print("Yes" if check_duplicate_within_k(arr, 3) else "No")   

# [Expected Approach] - Using HashSet - O(n) Time and O(k) Space
'''The idea is to use HashSet to store elements of the array arr[] and check if there is any duplicate present within a k distance. Also remove elements that are present at more than k distance from the current element. Following is a detailed algorithm.

Create an empty HashSet. 
Traverse all elements from left to right. Let the current element be 'arr[i]' 
If the current element 'arr[i]' is present in a HashSet, then return true. 
Else add arr[i] to hash and remove arr[i-k] from hash if i >= k'''

def checkDuplicateWithK(arr,k):
    #    create empty set 
    hash_set = set()
    # determine the length of the array
    n = len(arr)

    # transeverse the input array 
    for i in range(n):
    #    if the element is in the hashset found the duplicate
    #   else the add the element to the set and continue
        if arr[i] in hash_set:
           return True
        hash_set.add(arr[i])

    if (i  >= k):
           hash_set.remove(arr[i-k])
           return False
        
    # check case   
arr = [10, 5, 3, 4, 3, 5, 6]
print("Yes" if(checkDuplicateWithK(arr,3)) else "No")
