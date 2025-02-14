# find the number of unrepeated pairs 


elements = [1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6, 6, 6, 6, 6] 
n = len(elements)
s = 0 # sum number 
for i in range(0, n-1):
    s += bool(elements[i+1] - elements[i])
    # the term is repeated if the difference between the current term 
    # and the next term is 0 

    # calculate the number of differences that are greater than 0
    # bool makes the difference equal to 1 when the difference is 
    # greater than 1

print("number of unrepeated pairs: ", s * (s + 1) / 2)
