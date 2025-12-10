# native approch using temporary array -O(n) time and O(n) space
# step1: create an array of size input that is the same as the the input array 
# step 2 fill the array with the non zero index elements and then fill the remaining place with zeros
# step 3 finally copy all the elements from temoorary array to the input array

def pushZeroToEnd(arr):

    n = len(arr)
    temp = [0] * n

    # to keep track of the indec in temp[]
    j = 0

    # copy non-zero elements to the temp[]

    for i in range(n):
        if arr[i] != 0:
            temp[j] = arr[i]
            j += 1

    # fill the remaining position in temp[] with zeros
    while j < n:
        temp[j] = 0
        j += 1

    # copy all the elements from temp[] to arr[]
    for i in range(n):
        arr[i] = temp[i]

if __name__ == "__main__":
     arr = [1, 2, 0, 4, 3, 0, 5, 0]
     pushZeroToEnd(arr)

     for num in arr:
         print(num, end= " ")

