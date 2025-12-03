"""_summary_
"""

def days_to_units(num_days: int, unit_name: str):
    """Takes number of days and unit to convert days count to. Supports hours and minutes.

    Args:
        num_days (int): Number of days to convert
        unit_name (str): Unit type to convert to (hours, minutes)

    Returns:
        _type_: _description_
    """
    if unit_name == "hours":
        return f"{num_days} days are {num_days * 24} {unit_name} hours"
    if unit_name == "minutes":
        return f"{num_days} days are {num_days * 24 * 60} {unit_name} minutes"
    return "unsupported unit"

def validate_and_execute(input_dict: dict):
    """Validate user input and execute days to units conversion

    Args:
        input_dict (dict): Dictionary containing the number of days and unit to convert
    """
    try:
        days = input_dict["days"]
        unit = input_dict["unit"]
        if int(days) > 0:
            days = int(days)
            calculated_value = days_to_units(days, unit)
            print(calculated_value)
        else:
            print("Invalid input: Must be a whole positive number.")
    except ValueError:
        print("Invalid input: Must be a whole positive number.")

USER_INPUT_MESSAGE = "Enter a number of days and conversion unit.\n"
