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


def temp_conv(from_unit, to_unit, value) -> int | float:
    if from_unit == "celsius":
        celsius = value
    elif from_unit == "fahrenheit":
        celsius = (value - 32) * 5/9
    elif from_unit == "kelvin":
        celsius = value - 273.15
    else:
        raise ValueError()

    if to_unit == "fahrenheit":
        return (celsius * 9/5) + 32
    elif to_unit == "kelvin":
        return celsius + 273.15
    elif to_unit == "celsius":
        return celsius
    else:
        raise ValueError()


def convert_temperature(value, from_unit, to_unit) -> int | float:
    abs_zero = {
        'celsius': -273.15,
        'fahrenheit': -459.67,
        'kelvin': 0
    }
    if not isinstance(value, (float, int)) or isinstance(value, bool):
        raise ValueError()
    if not isinstance(from_unit, str) or not isinstance(to_unit, str):
        raise ValueError()
    from_unit, to_unit = from_unit.lower(), to_unit.lower()

    if not from_unit in abs_zero or not to_unit in abs_zero:
        raise ValueError()

    result = temp_conv(from_unit, to_unit, value)

    if result < abs_zero[to_unit]:
        raise ValueError()
    return result

