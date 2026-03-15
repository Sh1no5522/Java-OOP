import random
import string
print("****************Python Secet code encryption program*****************")
enc_dec = {}
enc_dec = dict(enc_dec)

numbers = " " + string.punctuation + string.digits + string.ascii_letters
numbers = list(numbers)
copy = numbers.copy()

random.shuffle(copy)
encrypted_code = ""
a = input("Enter a code to encrypt: ")
print("****************************************************************")
for num in a:
    index = numbers.index(num)
    encrypted_code += copy[index]
print("♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦")
print(f" Encrypted code is: {encrypted_code}")
print("♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦")
enc_dec[encrypted_code] = a
print("****************************************************************")
print(enc_dec)
print("****************************************************************")

t = input("Do you want to decrypt encrypted code(y/n): ")
print("****************************************************************")
if(t == "y"):
    r = True
    invalid_code_count = 0
    while r:
        c = input("Enter a code to decrypt: ")
        print("****************************************************************")
        if c in enc_dec.keys() :
            print("♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦")
            print(f"Secret Code is: ({enc_dec.get(c)})")
            print("♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦")
            r = False
        elif invalid_code_count >= 3:
            print("ALARM ENABLED!!! , HACKER FOUND!!! , DATA IS TRANSFERED TO THE MAIN HEADQUARTERS!!! ACCES BLOCKED!!!")
            print("****************************************************************")
            r = False
        else:
            print("Invalid encrypted code ,Enter again")
            print("****************************************************************")
            invalid_code_count += 1
else:
    print("Thanks for using our encryption program!")
    print("****************************************************************")