#Writing a program to tell customers how much to pay for orders of jollof rice.

while True:
    try:
        order = int(input("How many portions of Jollof Rice?: "))

        if order >= 10:
            print(f"Total: N{order * 800}, Bulk order; big discount.")
            break
        elif 5 <= order <= 9:
            print(f"Total: N{order * 1000}, Group order; small discount.")
            break
        elif 2 <= order <= 4:
            print(f"Total: N{order * 1200}, Standard price")
            break
        elif order == 1:
            print(f"Total: N{order * 1500} - Single portion")
            break
        elif order <= 0:
            print("Please enter a valid number. ")
    except ValueError: 
        print("Please enter a number: ")
        
        

    
    
