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
def check_duplicate_within_k(arr,k):
    
    fin = len(arr)
    for i in range(0,fin):
      for j  in range(i+1,fin):
         if arr[i] == arr[j] and abs(i-j) <= k:
            return True;
    return False


arr = [10, 5, 3, 4, 3, 5, 6]
print("Yes" if check_duplicate_within_k(arr, 3) else "No")          

