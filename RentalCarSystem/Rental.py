"""
Customer(s) who can:
• Inquire about available stock and prices,
• Rent a car,
• Return a car they have previously rented.

The Rental Shop(s) can:
• Issue a bill when the customer returns their car,
• Display available inventory and prices when a customer enquires,
• Process rent requests from customers after verifying stock availability.

"""
import os
import time

class RentalShop:

    "N.B. Jim is just a fake name"
    def __init__(self, rented_cars=[], cost = {"Hatchback": (30, 25), "Sedan": (50, 40), "Suv": (100, 90)}, car_dict={"Hatchback" : 4, "Sedan" : 3, "Suv" : 3}, name="Jim's Rental Shop"):

        self.rented_cars = rented_cars      # Array for storing details of clients renting cars. Initialised as an empty list
        self.cost = cost                    # Dictionary of tupples for the cost of renting each car for (Less than 1 week, More than 1 week)
        self.car_dict = car_dict            # Dictionary of cars and the number of them available at initialisation
        self.name = name                    # Name of Retal Shop
        self.cost_display = f"Hatchback: (£{self.cost["Hatchback"][0]} per day, £{self.cost["Hatchback"][1]} per day), Sedan: (£{self.cost["Sedan"][0]} per day, £{self.cost["Sedan"][1]} per day), (Suv: £{self.cost["Suv"][0]} per day, £{self.cost["Suv"][1]} per day)"
        self.cost_display = self.cost_display + "\nWith prices displayed as: (less than 7 days, more than 7 days)\nCustomers with loyalty cards only pay the 2nd amount and recieve a £10 discount"

    """Need to know :
        length of rental period
        Car rented
        Car's rental cost for rented period"""

    def initialisation_procedure(self):

        while True:
            print("Initialising Rental shop application......\n")
            time.sleep(1)
            x = input("Would you like to enter the name of your rental shop? Entering 'no' will leave the name as its default value:\n1. Yes\n2. No\n")
            x.strip()
            
            try:
                x = int(x)
                if (x != 1) and (x != 2):
                    raise ValueError
                elif x == 1:
                    new_name = input("\nPlease enter the new name of your rental shop:\n")
                    self.name = new_name
                    
                    # This command only works on windows systems and terminals and may produce an error on linux systems as their system may use "clear" instead of "cls"
                    # So i have included some simple conditional statements to prevent that error
                    if os.name == "nt":
                        os.system("cls") 
                    else:
                        os.system("clear")
                    print("Changing name and launching rental platform.....")
                    time.sleep(3)
                    if os.name == "nt":
                        os.system("cls") # This command only works on windows systems and terminals and may produce an error on linux systems as their system may use "clear" instead of "cls"
                    else:
                        os.system("clear")

                    return 0
                else:
                    # This command only works on windows systems and terminals and may produce an error on linux systems as their system may use "clear" instead of "cls"
                    # So i have included some simple conditional statements to prevent that error
                    if os.name == "nt":
                        os.system("cls") 
                    else:
                        os.system("clear")
                    return 0   
            
            except ValueError:
                print("Invalid value provided. Please enter 1 or 2 with no additional characters")


    "Return bill"
    def issue_bill(self, rental_period, car_rented, discount_cost=None, is_vip=False):

        if not is_vip:
            "String processing methods added to make entering the name into the command line simpler"
            car_rented = car_rented.strip()
            car_rented = car_rented.lower()
            car_rented = car_rented.title()

        
            "Conditional statements for handling which cost is used from the dictionary of tuples" 
            if rental_period > 7:
                i = 1
            else: 
                i = 0

            cost_per_day = self.cost[car_rented][i]
            total_cost = rental_period * cost_per_day
            return total_cost
        
        else:
            car_rented = car_rented.strip()
            car_rented = car_rented.lower()
            car_rented = car_rented.title()

            cost_per_day = discount_cost[car_rented]
            total_cost = rental_period * cost_per_day
            return total_cost
        
    "Fetch available car inventory"

    "Return available car inventory"
    def fetch_inventory(self):
        
        return self.car_dict

    # Because this is a display function and not a fetch function it does not return any value
    def display_prices(self):

        print("Prices displayed for renting one car of each model for rental periods: (less than 1 week, more than 1 week)\n")
        
        """
        The output of the below print will look like this:
            4 Hatchbacks at: ("£30 per day", "£25 per day") 
            3 Sedans at: ("£50 per day", "£40 per day")
            3 SUVs at: ("£100 per day", "£90 per day")
         
        """
        print(f"{self.car_dict["Hatchback"]} Hatchbacks at: {self.cost_dispaly["Hatchback"]}\n{self.car_dict["Sedan"]} Sedans: {self.cost_dispaly["Sedan"]}\n{self.car_dict["Suv"]} SUVs: {self.cost_dispaly["Suv"]}")

    # Return rental cost dict
    def fetch_rental_prices(self):

        return self.cost

    
    # Need to know car rented

    # Return tuple with relevant rental information ("Customer Name": str, Car rented: str, Customer info: dict) 
    def process_rent_request(self, car_to_rent, customer_name, period_to_rent=None):

        # A for loop to prevent customers already with 1 car from renting another car
        for client in self.rented_cars:
            if client["Customer Name"] == customer_name:
                print("\nYou have already rented a car. Please return it first before renting another\n")
                input("Press enter to return to main menu\n")
                
            
        if self.car_dict[car_to_rent] == 0:
            print("The car you wanted to rent is not available\n")
            return "Thank You"
        
        else:
            self.car_dict[car_to_rent] -= 1

        # Text formating to make sure keys match dictionary used
        car_to_rent = car_to_rent.lower()
        car_to_rent = car_to_rent.strip()
        car_to_rent = car_to_rent.title()

        self.rented_cars.append({"Customer Name": customer_name, "Rented Car": car_to_rent, "Period to rent": period_to_rent})
        
        return f"Car has been successfully hired, enjoy your new ride!\nIf you bring it back in {period_to_rent} days then you will owe: £{self.issue_bill(period_to_rent, car_to_rent)}\nIf you have a loyalty card you will owe: £{self.issue_bill(period_to_rent, car_to_rent, discount_cost={"Hatchback": (20), "Sedan": (35), "Suv": (80)}, is_vip=True)}"
        

    # Need to know car rented
    # Length of rental period

    def process_car_return(self, rental_period, customer_name, is_vip=False):

        # Return "False" if there have not been any cars rented yet
        if len(self.rented_cars) == 0:
            return "\nNo cars have been rented yet and so no cars can be returned\n"
        
        
        in_array = False    # Boolean for checking if this customer has rented a car yet

        if not is_vip:
            # Calculate the bill if the customer has indeed rented a car
            for client in self.rented_cars:
                if customer_name == client["Customer Name"]:
                    
                    bill = self.issue_bill(rental_period, client["Rented Car"])
                    in_array = True
                    break

        elif is_vip:
            for client in self.rented_cars:
                if customer_name == client["Customer Name"]:
                    
                    bill = self.issue_bill(rental_period, client["Rented Car"], discount_cost={"Hatchback": (20), "Sedan": (35), "Suv": (80)}, is_vip=True)
                    in_array = True
                    break

        # If there are no records of the customer renting a car return False
        if not in_array:
            return "You cannot return a car if you have not rented a car. Please rent a car first\n"
            
        
        # Return calculated bill
        i = 0
        while True:
            if self.rented_cars[i]["Customer Name"] == customer_name:
                self.car_dict[self.rented_cars[i]["Rented Car"]] += 1
                break
            i += 1

        del self.rented_cars[i]

        return f"Thank you for using our services, here is the bill for your rental period: {bill}"




class Customer:


    def __init__(self, name, address, phone_number):
        self.is_vip = False
        self.name = name
        self.address = address
        self.phone_number = phone_number


    # Call "fetch_inventory" method of RentalShop class and print returned value to screen
    def check_stock(self, shop: object):
        
        inventory = shop.fetch_inventory()
        inventory = f"{inventory["Hatchback"]} Hatchbacks, {inventory["Sedan"]} Sedans, {inventory["Suv"]}, SUVs"
        return inventory
    

    # Need to know what car the customer wants to check: 1. Hatchback, 2. Sedan, 3. SUV
    # Need to know rental period: More than 1 week, less than 1 week?

    # Call "display_prices" with relevant arguements and print result to screen and return dictionary of these prices
    def check_prices(self, shop: object):

        if os.name == "nt":
                os.system("cls") 
        else:
            os.system("clear")
        print(shop.cost_display)
        input("Press enter to continue")
        if os.name == "nt":
                os.system("cls") 
        else:
            os.system("clear")

    # Call "process_rent_request" and print rent request accepted if operation was success else print failed message
    def rent_car(self, car, shop: object, period=None):

        # Args: car_to_rent, customer_name, period_to_rent=None
        return_value = shop.process_rent_request(car_to_rent = car, customer_name = self.name, period_to_rent = period)
        
        return return_value

    # Call "process_car_return" function and print success if car was successfully returned else print fail message
    # Args: rental_period, customer_name process_car_return(self, rental_period, customer_name)
    def return_car(self, rental_period, customer_name, shop: object, is_vip=False):

        return shop.process_car_return(rental_period=rental_period, customer_name=customer_name, is_vip=is_vip)

# VIP class which is a child class of the "Customer" class and has a unique bill calculation method
class VIP(Customer):

    def __init__(self, name, address, phone_number):
        super().__init__(name, address, phone_number)
        self.is_vip = True
        discounted_costs = {"Hatchback": (20), "Sedan": (35), "Suv": (80)}
        self.discounted_costs = discounted_costs
        

    # # bill calculation method
    # def calculate_bill(self, rental_period, car_rented, discount_cost, is_vip=True):
    #     bill = super.issue_bill(rental_period, car_rented, discount_cost=self.discounted_costs, is_vip=self.is_vip)
