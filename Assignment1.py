def calculate_simple_interest(principal, rate):
    return (principal * rate) / 100

def get_interest_rate(gender, senior_citizen):
    if gender == 'female' and senior_citizen:
        return 8
    elif gender == 'female' and not senior_citizen:
        return 6
    elif gender == 'male' and senior_citizen:
        return 7
    elif gender == 'male' and not senior_citizen:
        return 5

def main():
    principal = float(input("Enter the principal amount: "))
    gender = input("Enter the customer's gender (male/female): ")
    senior_citizen = input("Is the customer a senior citizen? (yes/no): ")

    senior_citizen = senior_citizen.lower() == 'yes'

    rate = get_interest_rate(gender.lower(), senior_citizen)
    interest = calculate_simple_interest(principal, rate)

    print(f"The simple interest for the customer is: {interest}")

if _name_ == "_main_":
    main()