##  To write a program that analyses student's tests scores.

while True: # an outer loop opened so that the program can be repeated for another student
    
    while True: #loop opened for the first test score
        try: #to assign  the float input to the test score
            score_1 = float(input("Enter your 1st score: "))
            if 0 <= score_1 <= 100: #breaks try loop if the input is valid; if input is valid, try loop continues
                break
            print("Score out of range; must be between 0 and 100. ")
        except ValueError: #When the value entered is not a number
            print("Please enter a valid number: ")
            
    while True: #loop opened for the first test score
        try:
            score_2 = float(input("Enter your 2nd score: "))
            if 0 <= score_2 <= 100: #breaks try loop if the input is valid; if input is invalid, try loop continues
                break
            print("Score out of range; must be between 0 and 100. ")
        except ValueError: #When the value entered is not a number
            print("Please enter a valid number: ")

    while True:
        try:
            score_3 = float(input("Enter your 3rd score: "))
            if 0 <= score_3 <= 100:
                break
            print("Score out of range; must be within 0 and 100. ")  
        except ValueError:
            print("Please enter a valid number: ")
            
    average = (score_1 + score_2 + score_3) / 3
    
    if average >= 50:
        print("_" * 30)
        print("YOUR TEST RESULTS".center(30))
        print("_" * 30)
        print(f"Your 1st Test score: {score_1}")
        print(f"Your 2nd Test score: {score_2}")
        print(f"Your 3rd Test score: {score_3}")
        print("_" * 30)
        print(f"Your average is: {float(average):.2f}")
        print("_" * 30)
        print("REMARK: PASS")
    elif average < 50:
        print("_" * 30)
        print("YOUR TEST RESULTS".center(30))
        print("_" * 30)
        print(f"Your 1st Test score: {score_1}")
        print(f"Your 2nd Test score: {score_2}")
        print(f"Your 3rd Test score: {score_3}")
        print("_" * 30)
        print(f"Your average is: {float(average):.2f}")
        print("_" * 30)
        print("REMARK: FAIL")
        
    
    answer = input("Are you another student? yes/no: ")
    if answer.lower() != "yes":
        break
    
print("Thank You!")