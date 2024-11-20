from Rental import RentalShop as rs # Import RentalShop class
from Rental import Customer as cs
from Rental import VIP as vip
import os
import time

if __name__ == "__main__":

    first_itteration = True
    shop = rs()                         # Initialise RentalShop Instance
    itterate = True                     # Create boolean to allow for continuous menu re-use after errors or input
    customer_instance_dictionary = {}   # Customer instance array used to keep track of customers
    # shop.initialisation_procedure()     # Initialise shop
    i = 0                               # Set i to 0
    length_of_rental = {} 

    # A function for formatting the address
    def capitalize_address(string: str) -> str:
        string_array = []
        
        # For each word in the string, if the word is a number skip it else title the word
        for strings in string.split():

            # This prevents integers/numbers from beings passed through the .lower and .title methods and producing an error
            try: 
                strings = int(strings)
                strings = str(strings)
                string_array.append(strings)

            except ValueError:
                strings.lower()
                strings.title()
                string_array.append(strings)
            


        x = ""
        # Recombine the words into an address
        for words in string_array:
            x += " " + words 

        return x
    
    # A function for formatting the name of cars so that its acceptable for dictionary keys
    def title_words(string: str) -> str:

        string = string.lower()
        string = string.title()
        return string
    
    # Infinite loop for menu execution
    while itterate:
        if not first_itteration:
            input("Press enter to continue to main menu")
            if os.name == "nt":
                os.system("cls") 
            else:
                os.system("clear")
        first_itteration = False
        # This command only works on windows systems and terminals and may produce an error on linux systems as their system may use "clear" instead of "cls"
        # So i have included some simple conditional statements to prevent that error
        print(f"Welcome to {shop.name}\nHow can we help you today?\n")

        
        # The try allows for a more continuous menu experience if a non integer is entered then it will just loop back
        try:
            options = int(input("1. I would like to Rent a car\n2. I would like to return a car\n3. I would like to see what cars are available\n4. I would like to see the cost of renting your cars\n5. Exit platform\n"))

        # If value provided is not an integer then print an error message wait for key input and then clear console and continue
        except ValueError:
            
            print("Please enter valid option")
            input("Press enter to continue")
            if os.name == "nt":
                os.system("cls") 
            else:
                os.system("clear")
            continue
            
        # If option chosen is rent a car, execute following code that records customer information and 
        if options == 1:

            # Get customer information
            customer_name = input("\nPlease enter your name: ")
            address = input("\nPlease enter your address: ")
            number = input("\nPlease enter your phone number: ")

            customer_name = title_words(customer_name)    
            address = capitalize_address(address)

            # Record if customer is a vip, if they are a vip make sure to include 
            is_vip = int(input("Do you have a loyalty card?\n1. Yes\n2. No\n").strip())
            
            if is_vip == 1:
                customer_instance_dictionary[customer_name] = vip(customer_name, address, number)
            
            elif is_vip == 2:
                customer_instance_dictionary[customer_name] = cs(customer_name, address, number)

            else:
                raise ValueError

            while True:
                try:
                    car_choice = int(input("What car do you want to rent:\n1. Hatchback\n2. Sedan\n3. SUV\n4. Return to main menu\n").strip())

                    # If an invalid option is entered raise error
                    if (car_choice != 1) and (car_choice != 2) and (car_choice != 3) and (car_choice != 4):
                                raise ValueError
                                
                    period_to_rent = int(input("How long do you wish to rent the car?\n"))
                    # If invalid period to rent is entered raise error      
                    if (period_to_rent < 1):
                        raise ValueError

                    # If choice is Hatchback rent Hatchback for relevant customer instance
                    if car_choice == 1:
                        print(customer_instance_dictionary[customer_name].rent_car("Hatchback", shop, period=period_to_rent))
                        length_of_rental[customer_name] = period_to_rent
                        break
                    # If choice is Hatchback rent Sedan for relevant customer instance
                    if car_choice == 2:
                        print(customer_instance_dictionary[customer_name].rent_car("Sedan", shop, period=period_to_rent))
                        length_of_rental[customer_name] = period_to_rent                       
                        break

                    # If choice is Hatchback rent SUV for relevant customer instance
                    if car_choice == 3:
                        print(customer_instance_dictionary[customer_name].rent_car("Suv", shop, period=period_to_rent))
                        length_of_rental[customer_name] = period_to_rent                      
                        break
                    # If choice is to return to main menu just continue to main menu
                    if car_choice == 4:
                        break

                # If inavlid options are provided then print message and wait for user input then clear console and contiue to the beginning to the loop    
                except ValueError:
                    input("Invalid value provided. Please enter integer for car choice and positive integer for length of rental\nPress enter to continue\n")
                    if os.name == "nt":
                        os.system("cls") 
                    else:
                        os.system("clear")

        # If User wants to return their car start return process
        elif options == 2:

            # Get customer details to verify the correct car is returned
            customer_name = input("\nPlease enter your name:\n")
            customer_name = title_words(customer_name)

            is_vip = customer_instance_dictionary[customer_name].is_vip # int(input("Do you have a loyalty card?\n1. Yes\n2. No\n"))

            
            try:
                rental_period = length_of_rental[customer_name] # Fetch recorded rental period from dictionary

            # If there is no customer by entered name print message
            except KeyError:
                print(f"There is no customer by the name: {customer_name} in our system. Please try again")
                continue

            # Error catch for if string character is entered when trying to convert input to int
            try:
                opt = int(input(f"Is this the correct name rental period: {rental_period} days\n1. Yes\n2. No\n"))
                
                if opt == 2:
                    rental_period = int(input("Enter number of days car was used:\n"))

                # If rental period entered is 0 then raise error
                if rental_period <1:
                    raise ValueError
            
            # Error catch for invalid value passed
            except ValueError:
                input("Invalid value provided. Please enter positive integer for number of days and 1 or 2 for the rental period question.\nPress Enter to continue")

            # If the customer is a vip then make sure to provide the correct vip bill
            if is_vip:
                print(customer_instance_dictionary[customer_name].return_car(rental_period, customer_name, shop, is_vip=True))
                del length_of_rental[customer_name]
                input("Press Enter to return to main menu")

            # If they are not vip then issue bill at regular cost
            else:
                print(customer_instance_dictionary[customer_name].return_car(rental_period, customer_name, shop, is_vip=False))
                del length_of_rental[customer_name]
                input("Press Enter to return to main menu")

        # If they want to check what cars are available create dummy customer instance (this is required for check cost functionality)
        # and print available cars to screen
        elif options == 3:
            
            customer_instance = cs("John Doe", "Baker Street", None)
            if os.name == "nt":
                os.system("cls") 
            else:
                os.system("clear")
            print(customer_instance.check_stock(shop))
            input("Press Enter to continue")
            if os.name == "nt":
                os.system("cls") 
            else:
                os.system("clear")

        # Create dummy instance and display car prices
        elif options == 4:

            customer_instance = cs("John Doe", "Baker Street", None)
            if os.name == "nt":
                os.system("cls") 
            else:
                os.system("clear")
            customer_instance.check_prices(shop)
            input("Press Enter to continue")
            if os.name == "nt":
                os.system("cls") 
            else:
                os.system("clear")
               
        elif options == 5:
            exit()
        
        else:
            input("Invalid input provided please choose one of the 5 options\nPress enter to continue")
            if os.name == "nt":
                os.system("cls") 
            else:
                os.system("clear")
