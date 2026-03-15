import numpy as np
a = int(input("Enter amount coins: "))
is_running = True
count = 0
while is_running:
    count = 0
    if(a == 0):
        a = int(input("Enter number of coins again: "))
    if a >= 1:
        pass
    else:
        is_running = False
    x = np.random.choice([1,2,3,4,5], p=[0.225,0.225,0.1,0.225,0.225], size=(3))
    a -= 1
    print("••••••••••••••••••••••••••••••••••••••••••••")
    print(x)
    for i in x:
        if(i == 3):
            count += 1
    if(count == 3):
        print(f"Congratulations you won a prize!")
    print(f"Amount of coins left: {a}")
    b = input("Do you want to quit?(y/n): ")
    if b == "y":
        print("Thanks for playing our slot machine game")
        is_running = False
    else:
        pass