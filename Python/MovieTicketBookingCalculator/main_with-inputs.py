# I removed pre-set values ​​in the freeCodeCamp project task & I adjusted it again according with user inputs.

base_price = 15

# inputs
while True:
    try:
        age = int(input("What is your age: "))
        if age < 0:
            print('Age cannot be negative. Please try again.')
            continue
        break
    except ValueError:
        print('Invalid input! Please enter a valid number for your age.')

# age check
if age > 17:
    print('User is eligible to book a ticket')
else:
    print('User is not eligible to book a ticket.')
if age >= 21:
    print('User is eligible for Evening/Night shows')
else:
    print('User is not eligible for Evening/Night shows')
    
while True:
    seat_type = input("Which kind of seat do you want to sit (Gold or Premium): ").capitalize()
    if seat_type in ['Gold', 'Premium']:
        break
    print("Invalid seat type! Please choose either 'Gold' or 'Premium'.")
while True:
    show_time = input("Which showtime would you like to watch (e.g., Morning , Noon, Afternoon, Evening, Night): ").capitalize()
    if show_time in ['Morning','Noon','Afternoon', 'Evening', 'Night']: 
        break
    print("Invalid showtime! Please choose either Morning , Noon, Afternoon, Evening, Night.")
# membership and day check
while True:
    is_member_input = input("Are you a member (yes/no): ").strip().lower()
    if is_member_input in ['yes', 'y', 'true', '1', 'no', 'n', 'false', '0']:
        is_member = is_member_input in ['yes', 'y', 'true', '1']
        break
    print("Invalid input! Please answer with 'yes' or 'no'.")

is_weekend = True
while True:
    try:
        day = int(input("Which day of the week would you like to watch it? (1-7): "))
        if 1 <= day <= 7:
            if day in range(1, 6):  #1-5 weekdays
                is_weekend = False
            break
        print("Please enter a number between 1 and 7.")
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 7.")

# calculating discount
discount = 0
if is_member and age >= 21:
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')
print('Discount:', discount)

# calculating extra charges
extra_charges = 0
if is_weekend or show_time.capitalize() == 'Evening':
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')
print('Extra charges:', extra_charges)

# ticket booking 
if age >= 21 or (age >= 18 and (show_time.capitalize() != 'Evening' or is_member)):
    print('Ticket booking condition satisfied')

    service_charges = 0
    if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == 'Gold':
        service_charges = 3
    else:
        service_charges = 1
        
    print('Service charges:', service_charges)
    final_price = base_price - discount + extra_charges + service_charges
    print(f'Final price of ticket: {final_price}')
    
else:
    print('Ticket booking failed due to restrictions')

input("\nPress Enter to leave...")
