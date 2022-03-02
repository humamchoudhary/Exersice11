from random import *
List = [[randint(0, 5) for j in range(5)] for i in range(5)]
print(List)
Dict = {}
for i in range(5):
    count = 0
    for x in List:
        count += x.count(i)
    Dict.update({i: count})
print(Dict)
