def celsius_to_fahrenheit(celsius):
    # Write your code here
    return (celsius * 9/5) + 32
  
def fahrenheit_to_celsius(fahrenheit):
    # Write your code here
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    # Write your code here
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def temp_conv(from_deg, to_deg, value) -> int|float:
    if from_deg == "celsius":
        if to_deg ==  "fahrenheit":
            return (value * 9/5) + 32
        elif to_deg == "kelvin":
            return value + 273.15
        elif to_deg == "celsius":
            return value
    else:
        if from_deg ==  "fahrenheit":
            return (value - 32) * 5/9
        elif from_deg == "kelvin":
            return value - 273.15        


def convert_temperature(value, from_unit, to_unit) -> int|float:
    abs_zero={
        'celsius': -273.15,
        'fahrenheit': -459.67,
        'kelvin': 0
    }
    result = 0 
    if from_unit and to_unit:
        units = ((from_deg:=from_unit.lower()), (to_deg:=to_unit.lower()))
    else: 
        raise ValueError()

    if not isinstance(value, (float, int)) or isinstance(value, bool):
        raise ValueError()
    if from_deg == to_deg:
        if value >= abs_zero[to_deg]:
            return value 
        else:
            raise ValueError()

    if from_deg in abs_zero and to_deg in abs_zero:
        if from_deg == "celsius":
            result = temp_conv(from_deg, to_deg, value)
        else:
            temp_res = temp_conv(from_deg, to_deg, value)
            result = temp_conv("celsius", to_deg, temp_res)
        if result < abs_zero[to_deg]:
            raise ValueError()
        return result 
    else:
        raise ValueError()   
    
    # if units in valid_conv:
    #     result = valid_conv[units](value)
    #     if result < abs_zero[to_deg]:
    #         raise ValueError()
    #     return result 
    # else:
    #     raise ValueError()

        

