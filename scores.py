from cs50 import get_int

scores = []
for i in range(3):
    score = get_int("Score: ")
    scores.appemd(score)
    
avg = sum(scores) / len(scores)
print(f"Avg score: {avg}")