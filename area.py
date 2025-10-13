# лице и диаметър на окръжност по параметър а (радиус), като закръглим до 3ти знак след запетаята
import math

a = float(input("Please enter radius a:"))

diameter = 2 * a
P = round(math.pi * diameter, 3)
area = round(math.pi * (a ** 2), 3)

print(f"The area of the circle with radius {a} is {area}")
print(f"The perimeter of the circle with radius {a} is {P}")

