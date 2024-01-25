from cs50 import get_string

# 2 words input will result in an index > 16
# making the program think the Grade > 16

def main():
    text = get_string("Input text: ")
    
    letters = 0
    words = 0
    sentances = 0
    
    for i in text:
        if i.isalpha():
            letters += 1
        elif i == " ":
            words += 1
        elif i == "." or i == "!" or i == "?":
            sentances += 1
    
    # Not required to solve the problem
    print(f"Number of letters is: {letters}")
    print(f"Number of words is: {words + 1}") # not sure if we add +1 here or on line 7 but it works as is
    print(f"Number of sentances is: {sentances}")
    
    s = (letters / float(words) * 100)
    l = (sentances / float(words) * 100)
    
    index = round(0.0588 * s - 0.296 * l - 15.8)
    
    if index < 1:
        print("Before grade 1")
    elif index > 16:
        print("Grade 16+")
    else:
        print(f"Grade: {index}")
    
if __name__ == "__main__":
    main()
