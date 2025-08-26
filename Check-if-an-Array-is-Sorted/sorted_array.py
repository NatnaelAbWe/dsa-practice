# ITTRATIVE APPROCH

def sorted_array (arr):
    n = len(arr)
    c = 0
    while c < n -1 :
            if arr[c] <= arr[c+1]:
                c = c + 1
                continue
            else: 
                return False
                break
    return True
        