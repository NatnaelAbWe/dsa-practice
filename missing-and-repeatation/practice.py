'''Given an unsorted array arr[] of size n, containing elements from the range 1 to n, it is known that one number in this range is missing, and another number occurs twice in the array, find both the duplicate number and the missing number.

Examples: 

Input: arr[] = [3, 1, 3]
Output: [3, 2]
Explanation: 3 is occurs twice and 2 is missing.

Input: arr[] = [4, 3, 6, 2, 1, 1]
Output: [1, 5] 
Explanation: 1 is occurs twice and 5 is missing.'''

def searchRepeatAndMiss(arr):
    n = len(arr)
    result = []

    freeArr = [0] * (n+1)

    for num in arr:
        freeArr[num] += 1

    for i in range(1, n+1):
        if freeArr[i] == 0:
            result.append(i)
        elif freeArr[i] > 1:
            result.append(i)
        else:
            pass
    print(freeArr)
    return result

if __name__ == "__main__":
    arr = [3, 1, 3]
    answer = searchRepeatAndMiss(arr)
    print(answer)

def findTwoElement(arr):
    n = len(arr)
    repeat = -1

    for i in range(n):
        val = abs(arr[i])

        if arr[val - 1] > 1:
            arr[val - 1] = -arr[val - 1]
        else:
            repeat = val

    miss = -1
    for i in range(n):
        if arr[i] > 0:
            miss = i + 1
            break
    print(arr)
    return [repeat,miss]


if __name__ == "__main__":
    arr = [3, 1, 3]
    ans = findTwoElement(arr)
    print(ans[0], ans[1])