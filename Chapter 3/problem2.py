# problem2.py
# Que: to fill in a letter template given below with name and date.
letter = """
            Dear <|NAME|>,
            You are selected!,
            Date: <|DATE|>
            """

name = input("Enter your name: ")
date1 = input("Enter date: ")  # takes the string to use as a date

# use of the input function but checking the date validation as we don't want string
from datetime import datetime

date_obj = None  # none is used cause we want to check if the date is valid and expecting a date later
first_try = True  # to check if the user is entering the date for the first time or not

while True:
    if first_try:
        date = input("Enter date (YYYY-MM-DD): ")
        first_try = False
    else:
        date = input(
            "Invalid date format. Please enter date in YYYY-MM-DD format: \n or press Enter to exist: "
        )

        # allow exit only after the first try
        if date == "" and not first_try:
            print("Exiting the program.")
            break

        try:
            date_obj = datetime.strptime(
                date, "%Y-%m-%d"
            ).date()  # convert the string to a date object
            break  # exit the loop if the date is valid
        except ValueError:
            print("Invalid date format. Try again.")

# print only if valid date is entered
if date_obj:
    final_letter = letter.replace("<|NAME|>", name).replace("<|DATE|>", str(date_obj))
    print(final_letter)
