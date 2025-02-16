# find the number of unrepeated pairs 

# example list 
elements = [1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6, 6, 6, 6, 6] 
n = len(elements) # length of elements 
s = 0 # sum number 
for i in range(0, n-1):
    s += bool(elements[i+1] - elements[i])
    
    # the term is repeated if the difference between the current term 
    # and the next term is 0 

    # calculate the number of differences that are greater than 0
    # bool makes the difference equal to 1 when the difference is 
    # greater than 1

s = s * (s + 1) / 2

# the first 1 should be counted once, the second 1 should be counted twice
# in this example: 
# [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0]
# _____________________________________________________  # first addition  
#           ___________________________________________  # second addition
#                       _______________________________  # third addition 
#                                ______________________  # fourth addition 
#                                      ________________  # fifth addition 
# sum = 5 + 4 + 3 + 1 = 5 * (5 - 1) / 2

print("number of unrepeated pairs: ", s)
