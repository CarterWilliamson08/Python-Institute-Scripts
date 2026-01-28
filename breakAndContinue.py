"""
Design a program that uses a while loop and continuously asks the user to enter a word unless
the user enters "chupacabra" as the secret exit word, in which case the message "You've
successfully left the loop." should be printed to the screen, and the loop should terminate.
"""

while True:
    word = input("Enter a word: ")
    if word.lower() == "chupacabra":
        print("You've successfully left the loop.")
        break
