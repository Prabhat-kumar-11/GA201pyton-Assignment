# ### Problem **1: Print the following pattern**

# Write a program to print the following number pattern using a loop.

n = 4

for i in range(1, 6):
    sum_string = ""
    for j in range(1, i+1):
        sum_string += str(j)+" "
    print(sum_string)