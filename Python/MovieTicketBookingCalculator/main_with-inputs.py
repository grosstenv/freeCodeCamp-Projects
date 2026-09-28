# I removed pre-set values ​​in the freeCodeCamp project task & I adjusted it again according with user inputs.

base_price = 15

# inputs
age = int(input("What is your age: "))
seat_type = input("Which kind of seat do you want to sit (Gold or Premium): ")
show_time = input("Which showtime would you like to watch (e.g., Afternoon, Evening, Night): ")

# age check
if age > 17:
    print('User is eligible to book a ticket')

if age >= 21:
    print('User is eligible for Evening shows')
else:
    print('User is not eligible for Evening shows')

# membership and day check
is_member_input = input("Are you a member (yes/no): ").strip().lower()
is_member = is_member_input in ['yes', 'y', 'true', '1']

is_weekend = True
day = int(input("Which day of the week would you like to watch it? (1-7): "))
if day in range(1, 6):  # for weekdays
    is_weekend = False

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
