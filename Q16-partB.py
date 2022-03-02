inp = eval(input("Enter roman numrals: "))

roman = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D',
         1000: 'M', 4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'}
i = 0
rom_num = 0
while i < len(str(inp)):
    if i+1 < len(str(inp)) and inp[i:i+2] in roman:
        rom_num += roman[inp[i:i+2]]
        i += 2
    else:

        rom_num += roman[inp[i]]
        i += 1

print(rom_num)
