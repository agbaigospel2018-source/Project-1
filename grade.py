"""
1. Take an input asking the user to enter a score
2. Return A if the user's score is 70 and above
3. Return B if the user's score is between 60 and 69
4. Return C if the user's score is between 50 and 59
5. Return D if the user's score is between 40 and 49
6. Return E if the user's score is between 30 and 39
7. Return F if the user's score is less than 30
    """
    
score = float(input("Enter your score: "))

if 70 <= score <= 100:
    print("Grade: A")
elif 60 <= score <= 69:
    print("Grade: B")
elif 50 <= score <= 59:
    print("Grade: C")
elif 40 <= score <= 49:
    print("Grade: D")
elif 30 <= score <= 39:
    print("Grade: E")
elif score < 30:
    print("Grade: F")
else:
    print(f"Invalid score : {score}\nMust be between 0 and 100")
    
