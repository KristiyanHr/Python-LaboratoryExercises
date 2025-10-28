import random

elements = int(input("Enter a number of elements:"))

numbers = []

for i in range(elements):
    numbers.append(random.randint(1, 100))

new_list = []

for i in range(len(numbers) -1):
    new_list.append(numbers[i])
    sum_of_numbers = numbers[i] + numbers[i+1]
    new_list.append(sum_of_numbers)

print("Starting list",numbers)
print("New list",new_list)