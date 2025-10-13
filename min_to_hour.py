#да преобразуваме минути в часове

total_minutes = float(input("Please enter minutes: "))
days = total_minutes // 1440
remainingMinutes = total_minutes % 1440
hours = remainingMinutes // 60
minutes = remainingMinutes % 60

print(f"{hours} hours and {remainingMinutes} minutes")

#преобразуване на минути в дни часове и минути

print(f"{minutes} minutes is equal to {days} days, {hours} hours, and {minutes} minutes.")

