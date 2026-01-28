blocks = int(input("Enter the number of blocks: "))

#While loop practice

height = 0
needed = 1

while blocks >= needed:
    blocks -= needed
    height += 1
    needed += 1

print("Height of the pyramid:", height)