n = int(input("Enter a number:"))

numbers = list(range(1, n + 1))

reversed = numbers[::-1]
dict = {}

for i in range (n):
    dict[numbers[i]] = reversed[i]

print(dict)