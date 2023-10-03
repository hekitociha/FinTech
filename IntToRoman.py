def int_to_roman(num):

        value_to_roman = {
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

    roman_numeral = ''
    for value, roman_symbol in value_to_roman.items():
        while num >= value:
            roman_numeral += roman_symbol
            num -= value

    return roman_numeral

print(int_to_roman(1234))
