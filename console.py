# make a dict
# conversion function
# input

import os

TEMP_SCALE= {
    'Celsius': 'C',
    'Fahrenheit':'F',
    'kelvin': 'K'
}

def conversion_temperature(val, input_scale, output_scale):
    if input_scale == 'C':
        if output_scale == 'K':
            return val + 273.15
        elif output_scale == 'F':
            return (val * 9/5) + 32
        else:
            return f"I"

    elif input_scale == 'K':
        if output_scale == 'C':
            return val - 273.15
        elif output_scale == 'F':
            return ((val-273.15)*9/5)+32
        else:
            return f"I"

    elif input_scale == 'F':
        if output_scale == 'C':
            return (val - 32) * 5/9
        elif output_scale == 'K':
            return (((val-32)/1.8)+273.15)
        else:
            return f"I"

    else:
        return f"I"


while True:
    os.system('clear')
    print("\t\tpress 1 for conversion")
    print("\t\tEnter 2 to quit: ")
    choice = int(input("\t\t"))
    if choice == 1:
        value = float(input("\n\t\tEnter the value to be converted: "))
        input_unit = input("\n\t\tEnter the input Temperature Scale[C/F/K]: ").upper()
        output_unit = input("\n\t\tEnter the output Temperature Scale[C/F/K]: ").upper()
        result = conversion_temperature(value, input_unit, output_unit)
        if result == 'I':
            print("\n\n\t\tInvalid scale...")
        else:
            print(f"\n\n\t\tThe converted value of {value} {input_unit} = {result} {output_unit}")
            
        input("\n\n\t\tEnter to continue......")
    elif choice == 2:
        print(" \t\t!!!Thank you for your time to try this program!!! ")
        break
    else:
        print("\t\t...Invalid choice....")
        input("\n\n\t\tEnter to continue...")