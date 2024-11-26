# enigma.py
# description: a simple rotational ciphertext program that can create
# custom encoded messages, as well as encode and decode from file.
# author: Amellie
# created: 11.18.2024
# last update:  26.11.2024
import random

# String for the majority of translations. Majorly for taking the index of it.
alphabet = "abcdefghijklmnopqrstuvwxyz"

# User inputs a message and selects a key (or random), the message is then translated using the cipher
# the message is forced into lower case for simplicity and to avoid errors, it takes the input, takes the
# index of it, and shifts it according to the index of the alphabet. It also forces you to put a valid input because I
# am evil.
def encode_message():
    response = ""
    custominput = (input("Enter the message here:\n").lower())
    q = 1
    while q == 1:
        try:
            cipherkey = int(input("Enter the rotational cipher key:\n"))
            q = 0
        except ValueError:
            print("Put a valid rotational cypher key.\n")

    for char in custominput:
        try:
            letter = alphabet[(alphabet.index(char) + cipherkey) % 26]
            response += letter
        except ValueError:
            response += char
    print(response)



# Encodes a target file, similarly to encode_message, except now targeting a filename. It takes the file, opens it,
# reads it and stores tne text in a function in order to modify it. It is stored in usefulcontentfile and then shifted
# by the same block present in encode message. It transforms the text by writing the deciphered version into the file
# and ends up printing it.
def encode_file():
    fresponse = ""
    t = 0
    while t == 0:
        try:
            userfile = input("What text do you wanna access?\n")
            contentfile = open(userfile, "r")
            usefulconentfile = contentfile.read()
            fcipherkey = int(input("Enter the rotational cipher key:\n"))
            t = 1
        except FileNotFoundError:
            print("File not found.")

    for char in usefulconentfile:
        try:
            letter = alphabet[(alphabet.index(char) + fcipherkey) % 26]
            fresponse += letter
        except ValueError:
            fresponse += char

    contentfile = open(userfile, "w")
    contentfile.write(fresponse)
    contentfile = open(userfile, "r")

    print(contentfile.read())
    contentfile.close()




# Decodes target file using a user-specified key. If key is unknown, a keypress calls
# decode_unknown_key(). It uses the same block of code as encode file except it subtracts it if the key is known in order
# decypher it. Essentially works backwards.
def decode_file():
    dfresponse = ""
    t = 0
    while t == 0:
        try:
            dfuserfile = input("What text do you wanna access?\n")
            dfcontentfile = open(dfuserfile, "r")
            dfusefulconentfile = dfcontentfile.read().lower()
            t = 1
        except FileNotFoundError:
            print("File not found.")

        redirect = (input("Is the key known? (y/N)\n").lower())
        if redirect == "y":
            dfcipherkey = int(input("Enter the rotational cipher key:\n"))

            for char in dfusefulconentfile:
                try:
                    dfletter = alphabet[(alphabet.index(char) - dfcipherkey) % 26]
                    dfresponse += dfletter
                except ValueError:
                    dfresponse += char

            dfcontentfile = open(dfuserfile, "w")
            dfcontentfile.write(dfresponse)

            print("Your file has been decoded!")

        else:
            decode_unknown_key(dfuserfile)






# Runs if the key is unknown. It tries to print out an excerpt of 48 digits, if the text is less than the stated excerpt
# it subtracts until it is equal to the digit of the text. It deciphers the text by using the same block by the other
# functions. The for loop runs as long as the user does not have the key or states that the user does not have the key.
# once the user has the key, it sets i as the key and deciphers it. Furthermore, it also edits the file like previous
#functions.
def decode_unknown_key(filename):
    ex_len = 48
    df_contentfile = open(filename, "r")
    df_usefulcontentfile = df_contentfile.read().lower()

    for i in range(26):
        initialmessage = ""
        try:

            for char in df_usefulcontentfile[:ex_len]:
                try:
                    df_letter = alphabet[(alphabet.index(char) + i) % 26]
                    initialmessage += df_letter
                except ValueError:
                    initialmessage += char

        except IndexError:
            ex_len = ex_len - 1

        print(initialmessage)
        confirmation = input("Did I get it right?..... y/N\n")

        if confirmation == "y":

            key = i
            confirmedmessage = ""
            for char in df_usefulcontentfile:
                try:
                    df_letter = alphabet[(alphabet.index(char) + key) % 26]
                    confirmedmessage += df_letter
                except ValueError:
                    confirmedmessage += char

            df_contentfile = open(filename, "w")
            df_contentfile.write(confirmedmessage)
            print("Your text has been decoded")
# Break block that prohibits the function from overlapping with others.
            break


#Main function that prints out the functions.
def main():
    while True:
        print(f"Welcome to the Enigma Machine!\n"
              f"Please select an option:\n"
              f"[1]: Encode a custom message.\n"
              f"[2]: Encode file.\n"
              f"[3]: Decode file.\n"
              f"[4]: Exit.")

        selection = input("Choose an option:")
        if selection == "1":
            encode_message()
        elif selection == "2":
            encode_file()
        elif selection == "3":
            decode_file()
        elif selection == "4":
            print("Goodbye.")
            exit()
        else:
            print("Invalid choice. Please try again.")

# runs on program start
if __name__ == "__main__":
    main()