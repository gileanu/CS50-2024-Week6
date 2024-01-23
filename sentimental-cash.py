from cs50 import get_float

def main():
    while True:
        initAmount = get_float("Amount to convert into coins: ")
        if initAmount > 0:
            break
    
    initAmount = round(initAmount * 100)    
    
    coins = 0
    
    while initAmount >= 25:
        initAmount = initAmount - 25
        coins += 1
        
    while initAmount >= 10:
        initAmount = initAmount - 10
        coins += 1
        
    while initAmount >= 5:
        initAmount = initAmount - 5
        coins += 1
        
    while initAmount >= 1:
        initAmount = initAmount - 1
        coins += 1
        
    print(f"Total number of coins is: {coins}")
    
if __name__ == "__main__":
    main()