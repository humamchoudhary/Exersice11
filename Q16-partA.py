inp = input("Enter roman numrals: ")
inp = inp.upper()
roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
         'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
i = 0
dec_num = 0
while i < len(inp):
    if i+1 < len(inp) and inp[i:i+2] in roman:
        dec_num += roman[inp[i:i+2]]
        i += 2
    else:

        dec_num += roman[inp[i]]
        i += 1

print(dec_num)
