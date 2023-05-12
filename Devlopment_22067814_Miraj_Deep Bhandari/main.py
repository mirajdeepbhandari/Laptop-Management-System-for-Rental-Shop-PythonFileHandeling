# Importing necessary modules
import read as rd
import operation as op


#  Displaying the main menu to the user
def display_menu():
    '''It shows the Gui Main Menu to the user asking to start or close

       Returns:
       None
    '''
    # Printing the GUI
    print("+==================================================================================================================================+")
    print("|                                                                                                                                  |")
    print("|                                   #-----  Welcome to Miraj Laptop and Computer Shop -----#                                       |")
    print("|                                                                                                                                  |")
    print("|                                                     Kalanki-14, Kathmandu                                                        |")
    print("|                                                                                                                                  |")
    print("|                                           Contact Number:- 9844345562 , 01-43567800                                              |")
    print("|                                                                                                                                  |")
    print("+==================================================================================================================================+")
    print("|                                                                                                                                  |")
    print("|                                                    ...... Main Menu ......                                                       |")
    print("|                                                                                                                                  |")
    print("+----------------------------------------------------------------------------------------------------------------------------------+")
    print("|                                                                                                                                  |")
    print("|                                                           1) Start                                                               |")
    print("|                                                                                                                                  |")
    print("|                                                                                                                                  |")
    print("|                                                                                                                                  |")
    print("|                                                           2) Close                                                               |")
    print("|                                                                                                                                  |")
    print("+----------------------------------------------------------------------------------------------------------------------------------+")
    print("\n")
   

# Continuously displaying the main menu and allowing user interaction until the user chooses to exit
while True:
    # Displaying the main menu
    display_menu()

    # Getting user input to determine the next step
    user_choice = input(">> Enter your choice: ")
    print()
    print()

    if user_choice == '1':
       
        # Displaying the secondary menu
        while True:
            print()
            print("# CHOOSE THE OPTION WOULD YOU LIKE TO PERFORM --> \n")
            print("|=========================|")
            print("| Option |  Action        |")
            print("|=========================|")
            print("|   0    |  Show Stock    |")
            print("+-------------------------+")
            print("|   1    |  Sell          |")
            print("+-------------------------+")
            print("|   2    |  Order         |")
            print("+-------------------------+")
            print("|   3    |  Back          |")
            print("+-------------------------+")
            print("|   4    |  Close         |")
            print("+-------------------------+")
            print()
            
            # Getting user input to determine the next step
            sell_order_choice = input(">> Enter your choice: ")
            print()
            
            # Depending on the user's choice, execute the corresponding operation
            if sell_order_choice == '1':
                    
                    # Displaying the products and allowing the user to sell a product
                    op.username()
                    rd.display_products()
                    op.sell_products()

            elif sell_order_choice == '0':
                    
                    # Displaying the products available in stock
                    print("# THESE ARE THE AVAILABLE LAPTOPS IN THE STOCK --> \n")
                    rd.display_products()

            elif sell_order_choice == '2':
                   
                    # Displaying the products and allowing the user to order a product
                   rd.display_products()
                   op.order_products()

            elif sell_order_choice == '3':
                    
                     # If the user chooses to go back, break out of the secondary menu loop 
                    break
            
            elif sell_order_choice == '4':
                    
                     # If the user chooses to close the application, exit the program
                    exit()
            else:
                print("Invalid choice. Please enter a valid option.")
            
                
    elif user_choice == '2':
        exit()
    else:
        
        # If the user enters an invalid input, prompt them to enter a valid option
        print("Invalid choice. Please enter a valid option.")
        print()
   
