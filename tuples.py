starting_tuple = input("Enter the number to make tuple of: ")

normal_tuple = tuple(int(digit) for digit in starting_tuple)

reverse_tuple = tuple(int(digit) for digit in starting_tuple[::-1])

print("normal order:", normal_tuple)
print("reverse order:", reverse_tuple)