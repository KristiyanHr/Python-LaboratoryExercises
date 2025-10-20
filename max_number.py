N = int(input("Enter the number of N`s: "))

numbers = []

print("Enter the numbers:")

for i in range(N):
    num = int(input())
    numbers.append(num)

max_number = max(numbers)

print("The biggest number is: ", max_number)