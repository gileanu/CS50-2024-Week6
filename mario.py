'''
from cs50 import get_int

while True:
    h = get_int("Height: ")
    if h > 0:
        break
    
for i in range(h):
    print("#", end="")
'''

#for i in range(3):
#    print("?", end="")

#print("?" * 4)

for i in range(3):
    for j in range(4):
        print("#", end="")
        