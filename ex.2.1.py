# total = 0
# numbers_count = 0
#
# for i in range(7, 71):
#     if i % 3 == 0:
#         total += i
#         numbers_count += 1
#
# print("Average is: ", total / numbers_count)

#-------------------------------------Ex.3------------------------------------------------
#n = int(input("Please enter the number: "))
#
#first_digit = n // 10
#second_digit = n % 10

#f first_digit % 5 == 0:
#    print("First digit can be divided on 5 :", first_digit)
#else:
#    print("First digit can`t be divided on 5 :", first_digit)

#if second_digit % 2 == 0:
#   print("Second digit is even: ", second_digit)
#else:
#    print("Second digit is odd: ", second_digit)

#-------------------------------------Ex.4------------------------------------------------

# total = 0
#
# for i in range(1, 51):
#     if not i % 6 == 0 :
#         if i % 2 == 0 or i % 3 == 0:
#             total += i
#
# print(total)

#-------------------------------------Ex.5------------------------------------------------

# n = int(input("Enter number of N`s: "))
# min_value = 0
# max_value = 0
#
# for i in range(n):
#     number = int(input("Please enter a number: "))
#
#     if number < min_value:
#         min_value = number
#     elif number > max_value:
#         max_value = number
#
# print(min_value)
# print(max_value)

#-------------------------------------Ex.6------------------------------------------------

# shape_type = input("Моля въведете тип фигура(правоъгълен триъгълник, квадрат, правоъгълник")








#-------------------------------------Ex.7------------------------------------------------
#
# grades = float(input(" Enter your grades: "))
# payment = int(int(input("Enter the maximum amount of money in your university: ")))
#
# if grades >= 5.50:
#     print("For the following grades: ", grades, " you will get payment of: ", payment)
# elif grades >= 5.00 and grades < 5.50:
#     print("For the following grades: ", grades, " you will get payment of: ", payment * 0.7)
# elif grades >= 4.50 and grades < 5.00:
#     print("For the following grades: ", grades, " you will get payment of: ", payment * 0.5)
# elif grades < 4.50:
#     print("No cash for you this semester")

#-------------------------------------Ex.8------------------------------------------------

# gender = input("Enter the gender: ")
#
# if gender == "Male" or gender == "male":
#     capital = int(input("Enter your bank capital"))
#     if capital >= 250000:
#         print("Your bank capital is approved")
#     else:
#         print("Your bank capital is not approved")
# elif gender == "Female" or gender == "female":
#     size = int(input("Enter your breast size"))
#     if size >= 100:
#         print("You are approved")
#     else:
#         print("You are not approved")
#

#-------------------------------------Ex.9------------------------------------------------
#
# day = int(input("Enter the day (1- monday, 7 - sunday): "))
# n = int(input("Enter number of days: "))
#
# result = (day + n) % 7
#
# if result == 0:
#     result = 7
#
# days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# print("After ", n, "days it will be ", days[result -1])

#-------------------------------------Ex.10------------------------------------------------

# budget = float(input("Please enter your budget: "))
# season = input("Please enter the season")
# if budget <= 100:
#     destination = "Bulgaria"
#     if season == "summer":
#         spent = budget * 0.3
#         type_of_vacation = "Camp"
#     elif season == "winter":
#         spent = budget * 0.7
#         type_of_vacation = "Hotel"
# elif budget <= 1000:
#     destination = "Balkans"
#     if season == "summer":
#         spent = budget * 0.4
#         type_of_vacation = "Camp"
#     elif season == "winter":
#         spent = budget * 0.8
#         type_of_vacation = "Hotel"
# else:
#     destination = "Europe"
#     spent = budget * 0.9
#     type = "Hotel"
# print(f"Somewhere in {destination}")
# print(f"{type_of_vacation} - {spent:.2f}")

#-------------------------------------Ex.11------------------------------------------------

skiers = int(input("Enter the number of skiers: "))

for i in range(skiers):
    jackets = int(input("Enter number of jackets the skier will buy: "))
    helmet = int(input("Enter number of helmets skier will buy: "))
    shoes = int(input("Enter the number of shoes skier will buy: "))
    jackets_price = 120
    helmet_price = 75
    shoes_price = 299.90

    dds = (jackets_price + helmet_price + shoes_price) * 0.2
    total_price = (jackets_price + helmet_price + shoes_price )+ dds

print(f"The total price is: {total_price:.2f} lv")