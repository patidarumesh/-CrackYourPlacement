def intToRoman(num):
    roman_numerals = {
        1000: 'M',
        900: 'CM', 
        500: 'D', 
        400: 'CD',
        100: 'C', 
        90: 'XC', 
        50: 'L', 
        40: 'XL',
        10: 'X', 
        9: 'IX', 
        5: 'V', 
        4: 'IV', 
        1: 'I'
    }
    
    result = ''
    
    for value in sorted(roman_numerals.keys(), reverse=True):
        while num >= value:
            result += roman_numerals[value]
            num -= value
            
    return result

num = 3749
print(intToRoman(num))

# for i in range(1, 101):
#     print(i, ":", intToRoman(i))
