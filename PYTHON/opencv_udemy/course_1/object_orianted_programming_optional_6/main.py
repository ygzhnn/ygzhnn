from rent import CarRent, BikeRent, Customer

bike = BikeRent(100)
car = CarRent(10)
customer = Customer()

main_menu = True

while True:

    if main_menu:
        print("""
              ****** Vehicle Rental Shop ******
              A. Bike Menu
              B. Car Menu
              Q. Exit
              """)
        main_menu = False

        choice = input("Enter Choice: ")

    if choice == "A" or choice == "a":

        print("""
              ****** BIKE MENU ******
              1. Display Available Bikes
              2. Request a Bike on Hourly Basis $ 5
              3. Request a Bike on Daily Basis $ 84
              4. Return a Bike
              5. Main Menu
              6. Exit
              """)
        
        choice = input("Enter Choice: ")

        try:
            choice = int(choice)
        except ValueError:
            print("It is not integer")
            continue

        if choice == 1:
            bike.displayStock()
            choice = "A"
        
        elif choice == 2:
            customer.rentalTime_b = bike.rentHourly(customer.requestVehicle("bike"))
            customer.rentalBasis_b = 1
            main_menu = True
            print("---------------------")

        elif choice == 3:
            customer.rentalTime_b = bike.rentDaily(customer.requestVehicle("bike"))
            customer.rentalBasis_b = 2
            main_menu = True
            print("---------------------")

        elif choice == 4:
            bike.returnVehicle(customer.returnVehicle("bike"),"bike")
            customer.rentalBasis_b, customer.rentalTime_b, customer.bikes = 0,0,0
            main_menu = True
        
        elif choice == 5:
            main_menu = True

        elif choice == 6:
            break

        else:
            print("Invalid input please enter appropriate number [1,6]")
            main_menu = True

        
    if choice == "B" or choice == "b":

        print("""
              ****** CAR MENU ******
              1. Display Available Cars
              2. Request a cAR on Hourly Basis $ 10
              3. Request a Car on Daily Basis $ 192
              4. Return a Car
              5. Main Menu
              6. Exit
                """)
    
        choice = input("Enter Choice: ")

        try:
            choice = int(choice)
        except ValueError:
            print("It is not integer")
            continue

        if choice == 1:
            car.displayStock()
            choice = "B"
        
        elif choice == 2:
            customer.rentalTime_c = car.rentHourly(customer.requestVehicle("car"))
            customer.rentalBasis_c = 1
            main_menu = True
            print("---------------------")

        elif choice == 3:
            customer.rentalTime_c = car.rentDaily(customer.requestVehicle("car"))
            customer.rentalBasis_c = 2
            main_menu = True
            print("---------------------")            

        elif choice == 4:
            bike.returnVehicle(customer.returnVehicle("car"),"car")
            customer.rentalBasis_c, customer.rentalTime_c, customer.cars = 0,0,0
            main_menu = True
        
        elif choice == 5:
            main_menu = True

        elif choice == 6:
            break

        else:
            print("Invalid input please enter appropriate number [1,6]") 
            main_menu = True 

    elif choice == "Q" or choice == "q":
        break
    
    else:
        print("Invalid Input. Please Enter A-B-Q")
        main_menu = True

    print("Thank you for using the vehicle renting shop")

    

        
    