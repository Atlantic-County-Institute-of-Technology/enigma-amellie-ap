# enigma.py
# description: a simple rotational ciphertext program that can create
# custom encoded messages, as well as encode and decode from file.
# author: YOUR_NAME_HERE
# created: MM.DD.YYYY
# last update:  MM.DD.YYYY
import random

# we'll be using this string for the majority of our translations
alphabet = "abcdefghijklmnopqrstuvwxyz"

# user inputs a message and selects a key (or random), the message is then translated using the cipher
def encode_message():
    response = ""
    custominput = (input("Enter the message here:").lower())
    cipherkey = int(input("Enter the rotational cipher key:"))
    for char in custominput:
        try:
            letter = alphabet[(alphabet.index(char) + cipherkey) % 26]
            response += letter
        except ValueError:
            response += char
    print(response)
    pass

# encodes a target file, similarly to encode_message, except now targeting a filename
# def encode_file():
def encode_file():
    fresponse = ""
    t = 0
    while t == 0:
        try:
            userfile = input("What text do you wanna access?")
            contentfile = open(userfile, "r")
            usefulconentfile = contentfile.read()
            fcipherkey = int(input("Enter the rotational cipher key:"))
            t = 1
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

        except FileNotFoundError:
            print("File not found.")
        pass



# decodes target file using a user-specified key. If key is unknown, a keypress should
# call decode_unknown_key()
def decode_file():
    dfresponse = ""
    t = 0
    while t == 0:
        try:
            dfuserfile = input("What text do you wanna access?")
            dfcontentfile = open(dfuserfile, "r")
            dfusefulconentfile = dfcontentfile.read()
            dfcipherkey = int(input("Enter the rotational cipher key:"))

            for char in dfusefulconentfile:
                try:
                    dfletter = alphabet[(alphabet.index(char) - dfcipherkey) % 26]
                    dfresponse += dfletter
                except ValueError:
                    dfresponse += char

            dfcontentfile = open(dfuserfile, "w")
            dfcontentfile.write(dfresponse)
            dfcontentfile = open(dfuserfile, "r")

            print(dfcontentfile.read())
            dfcontentfile.close()

        except FileNotFoundError:
            print("File not found.")
        pass

# runs if the key is unknown. If this is true, print out all possible decoding combinations.
def decode_unknown_key(filename):


# main method declaration
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