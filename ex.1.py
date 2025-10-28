m = int(input("Enter a start number: "))
n = int(input("Enter an end number: "))

result = 1
for i in range(m,n):
    if i % 3 == 0 and i % 4 == 0:
        result *= i

print("The result: " ,result)