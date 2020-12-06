import os.path
import random

def generatePassword():
    chars = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHHIJKLMNOPQRSTUVWXYZ!@#$%^&*'
    password_length = 22
    password = ''

    for i in range(password_length):
        password += random.choice(chars)

    print("Your p is: " + password)
    return password

def checkExistence():
    if os.path.exists("psws.txt"):
        pass
    else:
        file = open("psws.txt", "w")
        file.close()
   
def appendNew():
    file = open("psws.txt", "a")

    web = input("Please enter the website: ")

    print()

    psw = generatePassword()

    file.write("----------------------------------------\n")
    file.write(web)
    file.write("\n")
    file.write(psw)
    file.write("\n")
    file.close

def main():
    checkExistence()
    appendNew()

main()
