# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word = input("What is your word? ")
for letter in user_word:
    # Complete the body of the for loop.
    if letter != 'a' and letter != 'e' and letter != 'i' and letter != 'o' and letter != 'u':
        print(letter)
    else:
        continue
