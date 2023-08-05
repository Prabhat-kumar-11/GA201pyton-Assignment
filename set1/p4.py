# 4. **Sum and Average**: Write a Python program that calculates and prints the sum and average of a list of numbers.
#     - *Input*: [10, 20, 30, 40]
#     - *Output*: "Sum: 100, Average: 25.0"


a = [10,20,10,20]

sum_value = 0

for i in a:
    sum_value +=i


average = sum_value/len(a)

print(sum_value,average)


