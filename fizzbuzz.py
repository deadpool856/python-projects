

for x in range (1,101):
    if x % 2 == 0 and x % 5 == 0:
        print("fizzbuzz")
    elif x % 2 == 0:
        print("fizz")
    elif x % 5 == 0:
        print("buzz")
    else:
        print(x)