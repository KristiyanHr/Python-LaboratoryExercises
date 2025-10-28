text = input("Enter the text: ")

symbol_count = {}

for char in text:
    if char in symbol_count:
        symbol_count[char] += 1
    else:
        symbol_count[char] = 1

print("Final Dict: ", symbol_count)
