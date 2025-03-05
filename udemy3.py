# number = int(input("Enter a number: " ))

# if number % 2 ==  0:
#     print("Even")
# else:
#     print("odd") 


# print("Weclome to Pyhton Pizza Deliveries!")
# size = input("What size pizza do you want? S,M or L: ").upper()

# bill = 0 

# if size == "S":
#     bill = 15
#     print("The bill for small pizza is $15")
# elif size == "M":
#     bill = 20
#     print("The bill for the meduim pzza is $20")
# elif size == "L":
#     bill = 25
#     print("The bill of the big pizza is $25")   
# else:
#     print("Sorry we dont offer what you want")

# pepperoni = input("Do yoy want pepperoni on pizza? Y or N: ").upper()
# if pepperoni == "Y":
#     if size  == "S":
#         bill += 2
#         print(f"The subtotal of the bill is ${bill}")
#     elif size == "M" or "L":
#         bill += 3
#         print(f"The subtotal of the bill is ${bill}")
#     else:
#         bill += 0
#         print(f"The subtotal of the bill is ${bill}")   
# else:
#     bill += 0
#     print(f"The subtotal of the bill is ${bill}")
    
    
# extra_cheese = input("Do you want extra cheese? Y or N: ").upper()
# if extra_cheese == "Y":
#         bill += 1
#         print(f"Your Final Bill ${bill}")
# else: 
#         bill += 0
#         print(f"Your Final Bill ${bill}")



    
print('''  
                      <>
        .-"""-.       ||::::::==========
       /= ___  \      ||::::::==========
      |- /~~~\  |     ||::::::==========
      |=( '.' ) |     ||================
      \__\_=_/__/     ||================
       {_______}      ||================
     /` *       `'--._||
    /= .     [] .     { >
   /  /|ooo     |`'--'|| 
  (   )\_______/      ||
   \``\/       \      ||
    `-| ==    \_|     ||
      /         |     ||
     |=   >\  __/     ||
     \   \ |- --|     ||
      \ __| \___/     ||
 jgs  _{__} _{__}     ||
     (    )(    )     ||
 ^^~  `"""  `"""  ~^^^~^^~~~^^^~^^^~^^^~^^~^ ''')


print("Mission Galatic Tresure Hunt")
print(''' 
You are Commander Alex Nova, an astronaut on a daring mission to recover an ancient alien artifact hidden on the distant planet Xylora Prime. This artifact, rumored to contain knowledge to unlock the secrets of the universe, is guarded by traps and riddles.

Your mission begins on your spaceship, Stellar Voyager, orbiting the planet. Your AI companion, Luna, offers you two options:

Decision 1: Landing Site
Crater Valley 1. A smooth, flat surface with minimal risks but eerie silence.
Glowing Ridge 2. A rugged terrain with strange glowing plants and potential hazards.

''')

decision = int(input("Choose any of the option 1 or 2: "))
if decision == 1:
    print('''
Outcome 1: Crater Valley
You choose Crater Valley, activating the autopilot. The descent is smooth, but as you step out onto the surface, the ground starts rumbling. Suddenly, a sinkhole opens beneath your feet! Game Over.

          ''')
    exit()
    
elif decision == 2:
    print('''
Outcome 2: Glowing Ridge
The glowing plants emit harmless light, guiding you to a hidden cave entrance. Inside, you find a holographic map that marks the artifact’s location. You proceed deeper into the planet.
          ''')
else:
    print("You must choose a valid option")

print('''
Decision 2: Obstacle in the Cave
1. Wait - Analyze the holographic map for hidden dangers.
2. Run Forward - Quickly navigate through the cave, trusting your instincts.
      ''')
decision2 = int(input("Choose any of the option 1 or 2: "))
if decision2 == 1:
    print('''
Outcome 1: Wait
You decide to wait. As you analyze the map, you notice faint symbols indicating a pressure-plate trap ahead. Carefully avoiding the plates, you proceed safely. Luna congratulates you on your patience.
          ''')

elif decision2:
    print('''
Outcome 2: Run Forward
You sprint ahead but fail to notice the pressure-plates. A trap activates, releasing a swarm of hostile drone beetles. They overwhelm you. Game Over.
          ''')
    exit()
print('''
Decision 3: Final Room The Artifact's Vault
You reach the artifact's vault, guarded by three glowing doors: Red, Blue, and Yellow.

    1. Red Door - The faint sound of roaring flames echoes from within.
    2. Blue Door - Chilling air seeps out, with faint growls in the distance.
    3.Yellow Door - A warm light shines, but its source is unclear.
      ''')
decision3 = int(input("Choose any of the option 1 or 2 and 3: "))
if decision3 == 1:
    print('''
Outcome 1: Red Door
You open the Red Door and are engulfed by an inferno. Game Over.
          ''')
    exit()
elif decision3 == 2:
    print('''
Outcome 2: Blue Door
The Blue Door reveals a chamber filled with ice beasts that charge at you. Game Over.
    ''')
    exit()
elif decision3 == 3:
    print('''
Outcome 3: Yellow Door
Behind the Yellow Door, you find the artifact suspended in a glowing field. As you reach out, Luna guides you through the process of safely extracting it. Triumphantly, you hold the artifact, its energy pulsating in your hands. You Win!
          ''')
