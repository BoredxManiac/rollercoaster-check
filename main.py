import lib_coasterimg as coasterimg
import time
import os

#Read check values
<<<<<<< HEAD
file_leeftijd = open("rules/age.txt", "r")
age_check = int(file1.read())
file_leeftijd.close()
=======
file_Age = open("rules/age.txt", "r")
age_check = int(file1.read())
file_Age.close()
>>>>>>> 516254c2f293a143a7fb37df36a5be0ac76c920f

file2 = open("rules/height.txt", "r")
height_check = int(file2.read())
file2.close()

running = True
while running:

    #Get inputs
    os.system('cls')
    print("Rollercoaster-check™")
    age = int(input("Voer leeftijd in: "))
    height = int(input("Voer lengte in: "))

    #Process checks
    if(age > age_check and height > height_check):
        os.system('cls')
        print("Stap maar in!")
        print(coasterimg.get())
        time.sleep(3)

    else:
        os.system('cls')
        print("Je voldoet niet aan de voorwaarden...")
        print(coasterimg.sad())
        time.sleep(1)

    result = input("Druk op Enter om nog een keer te checken, of X om te stoppen\n\n")
    if(result.upper() == "X"):
        running = False
