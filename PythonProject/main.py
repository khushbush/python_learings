calculation_to_units = 24
# name_of_unit = "hours"

def days_units(num_of_days,convertion_unit):
    if  convertion_unit =="hours":
        return f" {num_of_days} days are {num_of_days * 24} hours"
    elif convertion_unit =="minutes":
        return f" {num_of_days} days are {num_of_days * 24 *60} minutes"
    else:
        return "unsupported units"


def validate_and_execute():
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

user_input = ""
while user_input !="exit":
    user_input = input("Hay user, enter a number of days and I will convert it to hours!\n")
    # for num_of_days_element in user_input.split(","):
    #     validate_and_execute()

    days_and_units = user_input.split(":")
    print(days_and_units)
    days_and_unit_dictionary = {"days":days_and_units[0],"unit":days_and_units[1]}
    print(days_and_unit_dictionary)
    validate_and_execute()




