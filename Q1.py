dict = {}

while True:
    Prod = input(
        "Enter the name of the product or enter 1 to search again the code: ")
    if Prod == "1":
        break
    else:
        pass
    Price = eval(input(f"Enter the price of {Prod}: "))
    dict[Prod] = Price
print(dict)

while True:
    Prod_name = input("Enter the name of product: ")
    try:
        print(f"Price of {Prod_name} is {dict[Prod_name]}RS")
        input("enter 1 to exit or press enter to search again")
    except KeyError:
        print(f"Product {Prod_name} not found!")
    except:
        print("An error occurred!")
