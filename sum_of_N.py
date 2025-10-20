N = int(input("Enter number of N`s: "))

total = 0

print("Enter the numbers:")

for i in range(N):
    num = int(input())
    total += num

print("Sum of the numbers:", total)