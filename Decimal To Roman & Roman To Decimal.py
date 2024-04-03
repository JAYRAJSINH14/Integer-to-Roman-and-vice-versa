def roman_to_decimal(roman):
    roman_dict = {'I': 1, 'V': 5, 
                  'X': 10, 'L': 50, 
                  'C': 100, 'D': 500, 
                  'M': 1000}
    decimal = 0
    prev_value = 0
    for char in roman[::-1]:
        value = roman_dict[char]
        if value < prev_value:
            decimal -= value
        else:
            decimal += value
        prev_value = value
    return decimal

def decimal_to_roman(decimal):
    roman_dict = {1: 'I', 4: 'IV', 
                  5: 'V', 9: 'IX', 
                  10: 'X', 40: 'XL', 
                  50: 'L', 90: 'XC', 
                  100: 'C', 400: 'CD', 
                  500: 'D', 900: 'CM', 
                  1000: 'M'}
    roman = ''
    for value in reversed(list(roman_dict.keys())):
        while decimal >= value:
            roman += roman_dict[value]
            decimal -= value
    return roman

n = int(input("Enter 0 for Roman to Decimal conversion \n\t\t OR \nEnter 1 for Decimal to Roman conversion : "))

if(n==0):
    input_string = input("Enter space-separated values: ")
    input_list = input_string.split()
    for i in input_list:
        decimal_numeral = roman_to_decimal(i)
        print(f"{i} in decimal is: {decimal_numeral}")
elif(n==1):
    input_deci = input("Enter space-separated values: ")
    input_list = input_deci.split()
    for number_str in input_list:
        decimal_number = int(number_str)
        roman_numeral = decimal_to_roman(decimal_number)
        print(f"{decimal_number} in Roman numeral is: {roman_numeral}")
else:
    print("Please enter a valid choice")