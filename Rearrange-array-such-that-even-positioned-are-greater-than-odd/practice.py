'''Given an array arr[], sort the array according to the following relations:  

arr[i] >= arr[i - 1], if i is even, ∀ 1 <= i < n
arr[i] <= arr[i - 1], if i is odd, ∀ 1 <= i < n
Find the resultant array.[consider 1-based indexing]

Examples:  

Input: arr[] = [1, 2, 2, 1]
Output: [1 2 1 2]
 Explanation:
For i = 2, arr[i] >= arr[i-1]. So, 2 >= 1.
For i = 3, arr[i] <= arr[i-1]. So, 1 <= 2.
For i = 4, arr[i] >= arr[i-1]. So, 2 >= 1.

Input: arr[] = [1, 3, 2]
Output: [1 3 2]
Explanation: 
For i = 2, arr[i] >= arr[i-1]. So, 3 >= 1.
For i = 3, arr[i] <= arr[i-1]. So, 2 <= 3.'''

# approch 1 assign maximum element to even positions;

'''Observe that array consists of [n/2] even positioned elements. If we assign the largest [n/2] elements to the even positions and the rest of the elements to the odd positions, our problem is solved. Because element at the odd position will always be less than the element at the even position as it is the maximum element and vice versa. Sort the array and assign the first [n/2] elements at even positions.'''

def rearrangeArr(arr):
    # sort the array to order
    arr.sort()

    n = len(arr)
    res = [0] * n
    pt1, pt2 = 0, n-1

    for i in range(n):
        if (i + 1) % 2 == 0:
            res[i] = arr[pt2]
            pt2 -= 1
        else:
            res[i] = arr[pt1]
            pt1 += 1
    return res



'''[Approach 2] - Rearranging array by swapping elements
'''

def swampArr(arr):

    n = len(arr)
    for i in range(1, n):
        if (i + 1) % 2 == 0:
            if arr[i] < arr[i-1]:
                arr[i-1],arr[i] = arr[i],arr[i-1]
        else:
            if arr[i] > arr[i-1]:
                arr[i],arr[i-1] = arr[i-1],arr[i]


    return arr

if __name__ == "__main__":

    arr = [1, 2, 2, 1]
    res = rearrangeArr(arr)
    print(res)
    inputArr = [1,2,2,1,5.6]
    resultArr = swampArr(inputArr)
    print(resultArr)


