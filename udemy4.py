import random

# random_interger = random.randint(1,10)
# print(random_interger)

# random_number_o_to_1 = random.random()*10
# print(random_number_o_to_1)


# random_num = random.randint(1,100)
# print(random_num)


# if random_num % 2 == 0:
#     print("HEAD")
# else:
#     print("TAIL")


# random_num = random.randint(0,1)
# if random_num == 0:
#     print("head")
# else:
#     print("tail")

# friends = ["Alice","Bob","Charlie","David","Emanuel"]

# random1 = random.choice(friends)
# print(random1)

# random_index = random.randint(0, 4)
# print(friends[random_index])


handpick = int(input("what do you choose? Type 0 for rock, 1 for paper or 2 for scissors. \n"))

number = random.randint(0,2)




if handpick == 0:
    print(''' You Chose     
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___) 
          ''')
    if number == 1:
        print('''
              Computer Choose:
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
            You lose
              ''')
    elif number == 2:
        print('''
    _______    Computer Choose:
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
              YOU WON

              ''')
    else:
        print('''
                    Computer Choose:    
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___) 
                YOU DRAW

              ''')

elif handpick == 1:
    print('''
          You chose:
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
          ''')
    if number == 0:
        print('''
    _______    Computer Choose:
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___) 
              YOU WON
              ''')
    elif number == 1:
        print('''
                    Computer Choose:
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
                YOU DRAW
              ''')
    elif number == 2:
        print('''
 Computer Choose:
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
              YOU LOSE
              ''')
elif handpick == 2:
    print('''
   _______    You Choose:
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
        ''')
    if number  == 0:
        print('''
   _______    Computer Choose:
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___) 
              YOU LOSE

              ''')
    elif number == 1:
        print('''1
              
                   Computer Choose:
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
                YOU WIN
              ''')
    else: 
        number == 2
        print('''
    _______    Computer Choose:
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
              YOU DRAW

              ''')
else:
    print("You have to choose a valid one")
