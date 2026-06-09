
# name = "Ada"
# price = 500
# quantity_in_store = 12
# on_sale = True

# print(f"Name of customer: {name}")
# print(f"Price of product: ${price}")
# print(f"Quantity available: {quantity_in_store}")
# print(f"On sale: {on_sale}")

# numbers = [24, 16, 73, 8, 3, 9]
# numbers.sort()
# numbers.reverse()
# print(numbers)

# movies = ["The Flash", "Spiderman", "Captan America", "Hulk", "The Forge"]
# print(movies [2])
# movies.remove("The Flash")
# movies.insert(0, "Supergirl")
# movies.append("Fish Town")
# print(movies)

# book = {"Title": "In His Presence", "Author": "E.W. Kenyon", "Year": 1970, "Price": 5000}
# print(book["Author"])
# book["Price"] = 6000
# book["In-stock"] = True
# for key, value in book.items():
#     print(f"{key}: {value}")

# city = ("Tokyo", "Ottawa", "Lagos")
# print(city[1])
# x, y, z = city
# print (x)
# print(y)
# print(z)

# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# new =  set(numbers)
# print(new)
# numbers.sort()
# print(numbers)

# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# print(a & b)

# middle_name = None

# x = input("Do you have a middle name? yes/no: ").lower()

# if x == "yes":
#     middle_name = input("Enter your middle name: ")
# if middle_name is None:
#     print("No middle name")
# else: 
#     print(middle_name)

# num = input("Enter a number: ")

# print(num, type(num))

# num = int(num)
# print(num, type(num))

# num = float(num)
# print(num, type(num))

# total = 100
# print(total)

# total -= 30
# print(total)

# total *= 2
# print(total)

# total /= 5
# print(total)

# total //= 3
# print(total)


# list1 = ["Obi", "Ada", "Eric", "Olive"]
# list2 = [list1[x] for x in range(len(list1)) if x % 2 == 1 ]
# print(list2)
# csv = "Ada,22,87.5"
# fields = csv.split(",")
# print(fields)
# joined = "-".join(fields)
# print(joined)

# x = range(51)
# list1 = [i for i in x if i % 5 == 0]
# print(list1)
# message = "Hello, Python World!"
# print(message.startswith("Hello"))

# name = input("What is your full name?: ")
# print(name.strip())
# print(name.title())
# # print(name)
# print(name.split())
# # print(name)

# product_name = input("Enter product name: ")
# product_price = float(input("Enter prodcut price: "))
# quantity = int(input("Quantity to be purchased: "))
# total = product_price * quantity
# print("-" * 40)
# print(f"product name:\t\t{product_name} ")
# print(f"Product price:\t\tN{product_price:.2f}")
# print(f"Quantity purchased:\t\t{quantity}")
# print("-" * 40)
# print(f"Total:\t\tN{total:.2f}")

# print("I met Ada\'s father")

# print(0 and 42)
# name = input("Enter name: ") or Anonymous
# print(f"Hello {name}")

name = int(input("How old are you?: "))
if name < 13:
    print("Child")
elif 13 <= name <= 19:
    print("Teenager")
elif 20 <= name <= 64:
    print("Adult")
    employed = input("Are you employed? yes/no: ").lower()
    if employed == "yes":
        print("You are employed.")
    else:
        print("You are not employed.")
else:
    print("Senior")
