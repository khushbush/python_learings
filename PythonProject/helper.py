def days_units(num_of_days,convertion_unit):
    if  convertion_unit =="hours":
        return f" {num_of_days} days are {num_of_days * 24} hours"
    elif convertion_unit =="minutes":
        return f" {num_of_days} days are {num_of_days * 24 *60} minutes"
    else:
        return "unsupported units"


def validate_and_execute(days_and_unit_dictionary):
    try:
            user_input_number = int(days_and_unit_dictionary["days"])
            print(user_input_number > 0)
            if user_input_number > 0:
                calculated_values =  days_units(user_input_number,days_and_unit_dictionary["unit"])
                print(calculated_values)
                return calculated_values
            elif user_input_number == 0:
                return "you entered 0, please enter a positive number"
            else:
                return "you entered negative values!"
    except ValueError:
        print("Your input is not valid")





