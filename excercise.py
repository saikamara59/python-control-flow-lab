# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():
    # Your control flow logic goes here
    letter = input("enter a letter(a-z or A-Z):").lower()
    if len(letter) == 1 and letter.isalpha():
        vowels = "aeiou"
        if letter in vowels:
            print(f"The letter {letter} is a vowel.")
        else:
            print(f"the letter {letter} is a consonant.")  
    else:
         print("Invalid input. please enter a single alphabet letter")      
# Call the function
check_letter()


# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():
    # Set the minimum  age
    voting_age = 18
    
    age_input = input("Please enter your age: ")

    # Check if the input is a valid integer and handle invalid inputs gracefully
    if not age_input.isdigit():
        print("Please enter a valid number for your age.")
        return
    
    # Convert the input to an integer
    age = int(age_input)

    # Check if the age is non-negative and validate eligibility
    if age < 0:
        print("Age cannot be negative. Please enter a valid age.")
    elif age >= voting_age:
        print("You are eligible to vote!")
    else:
        print("Sorry, you are not old enough to vote.")

# Call the function
check_voting_eligibility()


# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    # Prompt the user to input the dog's age
    dog_age_input = input("Input a dog's age: ")

    try:
        # Convert the input to an integer
        dog_age = int(dog_age_input)

        # Validate that the dog's age is not negative
        if dog_age < 0:
            print("Age cannot be negative. Please enter a valid age.")
        elif dog_age <= 2:
            # If the dog is 2 years or younger, calculate dog years as 10 years per human year
            dog_years = dog_age * 10
        else:
            # If the dog is older than 2 years, calculate first 2 years as 10 dog years each, and subsequent years as 7 dog years each
            dog_years = 2 * 10 + (dog_age - 2) * 7

        # Print the calculated dog years
        print(f"The dog's age in dog years is {dog_years}.")
    
    except ValueError:
        # Handle the case where the input is not a valid integer
        print("Please enter a valid number for the dog's age.")

# Call the function
calculate_dog_years()


# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    # Your control flow logic goes here
    is_cold = input("Is it cold? (yes/no): ").strip().lower()
    is_raining = input("Is it raining? (yes/no): ").strip().lower()

    if is_cold == "yes" and is_raining == "yes":
        print("Wear a waterproof coat.")
    elif is_cold == "yes" and is_raining == "no":
        print("Wear a warm coat.")
    elif is_cold == "no" and is_raining == "yes":
        print("Carry an umbrella.")
    else:
        print("Wear light clothing.")
# Call the function
weather_advice()


# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():
    # Prompt for the month and day inputs
    month = input("Enter the month of the year (Jan - Dec): ").strip().lower()
    day = input("Enter the day of the month: ").strip()

    
    if month not in ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]:
        print("Invalid month. Please enter a valid month (Jan - Dec).")
        return
    
    # Validate day input
    if not day.isdigit() or int(day) < 1 or int(day) > 31:
        print("Invalid day. Please enter a valid day of the month.")
        return
    
    day = int(day)  
    
  
    if month in ["dec", "jan", "feb"]:
        # Winter: Dec 21 - Mar 19
        if month == "dec" and day >= 21 or month == "jan" or month == "feb" or (month == "mar" and day <= 19):
            season = "Winter"
        else:
            season = "Fall"
    elif month in ["mar", "apr", "may"]:
        # Spring: Mar 20 - Jun 20
        if month == "mar" and day >= 20 or month == "apr" or month == "may" or (month == "jun" and day <= 20):
            season = "Spring"
        else:
            season = "Winter"
    elif month in ["jun", "jul", "aug"]:
        # Summer: Jun 21 - Sep 21
        if month == "jun" and day >= 21 or month == "jul" or month == "aug" or (month == "sep" and day <= 21):
            season = "Summer"
        else:
            season = "Spring"
    elif month in ["sep", "oct", "nov"]:
        # Fall: Sep 22 - Dec 20
        if month == "sep" and day >= 22 or month == "oct" or month == "nov" or (month == "dec" and day <= 20):
            season = "Fall"
        else:
            season = "Summer"
    
    # Print the season for the entered date
    print(f"{month.capitalize()} {day:02d} is in {season}.")

# Call the function to test
determine_season()










