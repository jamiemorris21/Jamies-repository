print("We have a range of holiday destinations for you to choose from:") # showing the user the options
print("London")
print("Amsterdam")
print("Paris")
print("Rome")
print()

destinations = ['London', 'Amsterdam', 'Paris', 'Rome'] # list of destinations for ease
flight_prices = {'London': 150, 'Amsterdam': 175, 'Paris': 100, 'Rome': 85} # dictionary of flight prices per destination 
hotel_prices = {'London': 50, 'Amsterdam': 75, 'Paris': 80, 'Rome': 65} # dictionary of hotel prices per destination
car_rental_prices = {'London': 25, 'Amsterdam': 30, 'Paris': 15, 'Rome': 10 } # dictionary of car rental prices per destination

city_flight = input("Where would you like to go on holiday?: ") # asking the user for their choice of destination
city_flight = city_flight.capitalize()

while city_flight not in destinations:
    print("Sorry that's not a destination we fly to. Please enter another destination. ")
    city_flight = input("Where would you like to go on holiday?: ") # adding error loop to check for correct input

while True:
    try:
        num_nights = int(input("How many days would you like to stay for?: ")) # length of stay, in loop checking for an integer
        break
    except ValueError:
        print("Sorry we didn't recognise that. Please enter a number. ")

while True:
    try:
        rental_days = int(input("How many days would you like to hire a car for?: ")) # length of care hire, in loop checking for an integer
        break
    except ValueError:
        print("Sorry we didn't recognise that. Please enter a number. ")
 
def hotel_cost(): # defining the function for calculating the hotel cost
    return hotel_prices[city_flight] * num_nights # calling the dictionary of hotel prices & multiplying by user inputted num of nights

def plane_cost(): # function for calculating plane costs
    return flight_prices[city_flight]

# I thought this way would be more efficient than using if/elif because if they wanted to add a new destination it would involve less rewriting of code

'''def plane_cost()
    if city_flight == 'London':
        x = 150
    elif city_flight == 'Amsterdam':
        x = 175
    elif city_flight == 'Paris':
        x = 100
    elif city_flight == 'Rome':
        x = 85
    return x'''

# just showing I can do it this way too :)

def car_rental(): # function for calculating hotel rental cost
    return car_rental_prices[city_flight] * rental_days # calling the dictionary of rental prices & multiplying by user inputted num of rental days

def holiday_cost(): # function for calculating total holiday cost
    total = hotel_cost() + plane_cost() + car_rental() # calling the 3 different functions already declared and adding together
    print()
    print(f"The total cost of your holiday to {city_flight} is £{total}.") # printing the total output
    print(f"Your flight cost is £{plane_cost()}.")
    print(f"Your hotel cost for {num_nights} nights is £{hotel_cost()}.")
    print(f"Your car rental cost for {rental_days} days is £{car_rental()}.")
    print("Enjoy your trip!")

holiday_cost() # calling the final function to print out
