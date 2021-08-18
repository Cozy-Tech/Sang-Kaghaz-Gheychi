import random

user_score = 0
computer_score = 0

choices = ["sang","kaghaz","gheychi"]

while True:
    user_choice = input("Lotfan beyne SANG | KAGHAZ | GHEYCHI yeki ro entelhab kon (Baraye khoruj benevis q) => ").lower()
    if user_choice == "q":
        break

    if user_choice not in choices:
        print("Invalid input!, Try Again.")
        continue

    random_choice = random.randint(0,2)
    computer = choices[random_choice]
    print(f"Entekhabe Computer ==> {computer}")

    if user_choice == computer:
        print(f"Mosavi Shod! Dobare Boro ...")

    elif user_choice == "sang" and computer == "gheychi":
        print(f"Afarin! To barande shodi =) | +1 emtiaz!")
        user_score += 1

    elif user_choice == "kaghaz" and computer == "sang":
        print(f"Afarin! To barande shodi =) | +1 emtiaz!")
        user_score += 1

    elif user_choice == "gheychi" and computer == "kaghaz":
        print(f"Afarin! To barande shodi =) | +1 emtiaz!")
        user_score += 1

    else:
        print("Sharmande! Computer barande shod! =(")
        computer_score += 1


print(f"To {user_score} Bordi!")
print(f"Computer Ham {computer_score} Bord!")