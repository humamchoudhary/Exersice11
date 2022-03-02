dict = [{'name': 'Todd', 'phone': '555-1414', 'email': 'todd@mail.net'},
        {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
        {'name': 'Princess', 'phone': '555-3141', 'email': ''},
        {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@mail.net'}]

print("===== PART A =====")
for i in dict:
    if i['phone'][-1:] == '8':
        print(i['name'])
print("===== PART B =====")
for i in dict:
    if i['email'] == '':
        print(i['name'])
