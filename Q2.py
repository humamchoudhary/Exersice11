# letting that this is the dict from the previous question
Dict = {"Bubble": 2, "Toffee": 0.25, "Chips": 5}
Price = eval(input("Enter the price: "))
for i in Dict:
    if Dict[i] < Price:
        print(f"Product: {i} || Price: {Dict[i]}$")
