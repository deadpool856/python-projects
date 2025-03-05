# print(len("hello"))


#

#subscripting
# print("hello"[4])
# print("hello"[-1])


#integer = whole number

# print(123 + 345)


#larger number
# print(123_456_789)


#float = floating point number
# print(3.14159)

#boolean
# print(True)
# print(False)

# print(len(str(12345)))

#types of datatypes
# print(type(123))
# print(type("123"))
# print(type(22.2))
# print(type(True))

# print("Number of letters in your name: " +  str(len(input("Enter your name "))))


# print("my age: " + str(12))
# print(123 + 456)
# print(7 -3)
# print(5 * 4)
# print (5 / 3)
# print(5 // 3)
# print(3**4)
#

# print(3*3+3*3-3)

# bmi = 84 / 1.65 ** 2
# print(bmi)
# print(round(bmi))
# print(round(bmi,2))


# score = 0

# #user scores a point
# score += 1
# print(score)


# f-strings
# score = 0
# height =2.8
# is_winning =True
# print(f"Your score is = {score}, your height is {height}, and you are winning {is_winning}"  )

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
split = int(input("How many people to split the bill? "))


bill_tip = (bill * (tip/100)+ bill)
print(bill_tip)
total_bill= (bill_tip/split)

print(f"Each person should pay: ${total_bill: .2f}" )



