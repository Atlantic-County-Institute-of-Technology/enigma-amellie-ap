# enigma.py
# description: a simple rotational ciphertext program that can create
# custom encoded messages, as well as encode and decode from file.
# author: YOUR_NAME_HERE
# created: MM.DD.YYYY
# last update:  MM.DD.YYYY
import random

# we'll be using this string for the majority of our translations
alphabet = "abcdefghijklmnopqrstuvwxyz"
response = ""

# user inputs a message and selects a key (or random), the message is then translated using the cipher
def encode_message(v_custominput, v_cipherkey, a):
    for i in range(0,len(alphabet):
        letter = (v_custominput) + v_cipherkey)
    pass

# encodes a target file, similarly to encode_message, except now targeting a filename
def encode_file():
    pass

# decodes target file using a user-specified key. If key is unknown, a keypress should
# call decode_unknown_key()
def decode_file(v_custom):
    pass

# runs if the key is unknown. If this is true, print out all possible decoding combinations.
def decode_unknown_key(filename):
   pass


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
            custominput = (input("Enter the message here:"))
            cipherkey = int(input("Enter the rotational cipher key:"))
            encode_message(custominput, cipherkey, i)
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