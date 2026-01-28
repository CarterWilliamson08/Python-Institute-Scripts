#Secret Number Loop Pracice

secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

guess = 0

while guess != secret_number:
    guess = int(input("Please enter a number: "))
    if guess == secret_number:
            print("Well done, muggle! You are free now.")
    else:
        print("Ha ha! You're stuck in my loop!")