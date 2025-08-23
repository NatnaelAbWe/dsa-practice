"""Given an array arr[] of size n, the task is to find all the Leaders in the array. An element is a Leader if it is greater than or equal to all the elements to its right side.

Note: The rightmost element is always a leader.

Examples:

Input: arr[] = [16, 17, 4, 3, 5, 2]
Output: [17 5 2]
Explanation: 17 is greater than all the elements to its right i.e., [4, 3, 5, 2], therefore 17 is a leader. 5 is greater than all the elements to its right i.e., [2], therefore 5 is a leader. 2 has no element to its right, therefore 2 is a leader.

Input: arr[] = [1, 2, 3, 4, 5, 2]
Output: [5 2]
Explanation: 5 is greater than all the elements to its right i.e., [2], therefore 5 is a leader. 2 has no element to its right, therefore 2 is a leader."""

# the native approch : using a nessted loop
# time complexity - o(n)
# Auxilary space complexity - o(1)

def leader_Array(arr):
    res = list()
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] < arr[j]:
                break
        else:
            res.append(arr[i])

    return res


# Expected Approch using the suffix maximum 
# time complexity - o(n)
# Auxilary space complexity - o(1)

def leader_array_solution(arr):

    res = list()
    n = len(arr)

    for i in range(n):
        if i == n - 1:
            res.append(arr[i])
        elif arr[i] >= max(arr[i+1:]):
             res.append(arr[i])
    return res





