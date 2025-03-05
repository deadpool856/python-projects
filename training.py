
def main():
    name = input("enter your name: ")
    age = int(input("Enter your age: "))
    stid = int(input("enter your student id: " ))
    print(name, age, stid)
    option = input("is the informtion is correct: y/n ")
    if option == "y":
        print("very well ")
        
    else:
        return main()

def question():
    print()
    





if __name__ == "__main__":
              main()
               
