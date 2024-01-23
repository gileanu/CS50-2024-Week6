from cs50 import get_int

while True:
    height = get_int("Height: ")
    width = height
    if height > 0 and height <= 8:
        break

for i in range(0, height):
    hash = i + 1
    space = width - hash

    print(" " * space, end="")
    print("#" * hash, end="")
    print(" ", end="")
    print(" ", end="")
    print("#" * hash)