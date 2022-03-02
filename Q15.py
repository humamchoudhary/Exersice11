from ast import Mod


Dict = {
    "Eastern": {
        "Central": 1,
        "Mountain": 2,
        "Pacific": 3,
    },
    "Central": {
        "Eastern": -1,
        "Mountain": 1,
        "Pacific": 2,
    },
    "Mountain": {
        "Eastern": -2,
        "Central": -1,
        "Pacific": 1,
    },
    "Pacific": {
        "Eastern": -3,
        "Central": -2,
        "Mountain": -1,
    },
}
Time = 0

time = input("Enter time in Hour:Minutes(am/pm): ")
s_zone = input("Enter the name of current zone: ")
e_zone = input("Enter the name of desired zone: ")
Time = time.split(':')
Next_time = Dict[s_zone][e_zone]+int(Time[0])

if int(Next_time) > 12:
    l = len(Time[1])
    Next_time = Next_time % 12
    if Time[1][l-2:].lower() == "am":
        Mode = "pm"
    elif Time[1][l-2:].lower() == "pm":
        Mode = "am"
print(f"{Next_time}:{Time[1][:2]} {Mode}")
