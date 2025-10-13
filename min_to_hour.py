#да преобразуваме минути в часове

minutes = float(input("Please enter minutes: "))
hours = minutes // 60
remainingMinutes = minutes % 60

print(f"{hours} hours and {remainingMinutes} minutes")
