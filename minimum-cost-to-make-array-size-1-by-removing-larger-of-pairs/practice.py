# pyrhon program to find the minimum
# cost to reduce array size to 1
# function to calculate the minimum cost


def cost(a):
    # minimum cost is n-1 multiplied
    # with minimum element
    # determine the length of the array and store it to the 
    l = len(a)

    return ((l-1) * min(a))


# driver code
a = [ 4, 3, 2 ,5,1]
print(cost(a))

