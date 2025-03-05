import random

word_list = ["aardvark","baboon" , "camel"]

chosen_word = random.choice(word_list)

placeholder  = ""
word_len = len(chosen_word)

lives = 6

for position in range(word_len):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letter = ""   
while not game_over:
    guess = input("Guess a letter: \n").lower()

    display = ""


    for x in chosen_word:
        if x == guess:
            display += x
            correct_letter += guess
        elif x in correct_letter:
            display += x
        else: 
            display += "_"

    print(display)


    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose. ")

    if "_" not in display:
        game_over = True
        print("You win.") 



