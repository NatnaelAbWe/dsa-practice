'''Given an array of n integers, find the 3 elements such that a[i] < a[j] < a[k] and i < j < k in 0(n) time. If there are multiple such triplets, then print any one of them.

Examples:  

Input: arr[] = {12, 11, 10, 5, 6, 2, 30}
Output: 5, 6, 30
Explanation: As 5 < 6 < 30, and they 
appear in the same sequence in the array 

Input: arr[] = {1, 2, 3, 4}
Output: 1, 2, 3 OR 1, 2, 4 OR 2, 3, 4
Explanation: As the array is sorted, for every i, j, k,
where i < j < k, arr[i] < arr[j] < arr[k] 

Input: arr[] = {4, 3, 2, 1}
Output: No such triplet exists.'''

def find_sorted(arr):
    n = len(arr)
    max = n - 1
    min = 0

    smaller = [0] * 10000
    smaller[0] = -1

    for i in range(1,n):
        if  arr[i] <= arr[min]:
            min = i
            smaller[i] = -1
        else:
            smaller[i] = min

    
    greater = [0] * 10000
    greater[0] = -1

    for i in range(1,n):
        if  arr[i] >= arr[max]:
            max = i
            greater[i] = -1
        else:
            greater[i] = max

    for i in range(0, n):
        if smaller[i] != -1 and greater[i] != -1:
            print(arr[smaller[i]], arr[i], arr[greater[i]])
            return
        
    print("No triplet found")
    return

arr = [12, 11, 10, 5, 6, 2, 30]
find_sorted(arr)