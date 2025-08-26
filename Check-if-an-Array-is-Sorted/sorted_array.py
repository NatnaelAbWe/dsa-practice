# ITTRATIVE APPROCH

def sorted_array (arr):
    n = len(arr)
    count = 0
    while count < n -1 :
            if arr[c] <= arr[c+1]:
                c = c + 1
                continue
            else: 
                return False
                
    return True

# Recursive Approch 

def is_sorted_helper(arr, n):

    #  base case
    if (n == 0 or n == 1):
         return True
    
    # chceck if the current and the previous elements are in order
    # and recrusively check the rest of the Arrays

    is_sorted_helper(arr[n] >= arr[n-1] and is_sorted_helper(arr, n-1))

def is_sorted(arr):
     n = len(arr)

     return is_sorted_helper(arr, n)
        