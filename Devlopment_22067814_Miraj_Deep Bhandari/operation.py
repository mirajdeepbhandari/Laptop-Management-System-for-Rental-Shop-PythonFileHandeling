import read as rd
import write as wr


name_=""
noOfItems=""
customername_=""
sell_count=0
issingleSell=True
mul_sell=[]
ship=None

#sell product method
def sell_products():
    """
    Function to sell laptops from the inventory.

    This function allows the user to sell laptops from the inventory. It prompts the user to enter the ID of the laptop they want to sell, 
    the number of items they want to sell, and whether they want to continue selling or not. Once the user confirms that they want to sell 
    the item(s), it updates the inventory accordingly and generates a sell invoice.

    Returns:
    None
    """
  
    global mul_sell
    multiple_sells=[]
    sell = True
    while sell:

        global id_   # initialize id_ to None
        while True:
            
            # Prompt user to input the ID of the laptop they want to sell
            print()
            print("+-----------------------------------------------------------------------------------------------+")
            id = input("Enter the ID of the laptop You Want To Sell: ")
            print("+-----------------------------------------------------------------------------------------------+")
            print()

            # Check if the entered ID is in the inventory, if not prompt the user to enter a valid ID
            for laptop_info in rd.datalist:
                if id in laptop_info:  # check if id is in the current laptop's info
                    id_ = id  # set id_ to id
                    break  # break out of the inner loop
            else:  # executed when the inner loop completes without finding a match
                print()
                print("+-----------------------------------------------------------------------------------------------+")
                print("OPPS! No laptop found. Enter a valid ID!")
                print("+-----------------------------------------------------------------------------------------------+")
                print()
                continue  # continue to the next iteration of the outer loop
            break  # break out of the outer loop

        global noOfItems
        while True:
         try:
             global sell_count
             # Prompt user to input the number of items they want to sell
             print()
             print("+-----------------------------------------------------------------------------------------------+")
             sell_count = int(input(">> How many items do you want to Sell: "))
             print("+-----------------------------------------------------------------------------------------------+")
             print()
             # Check if the entered number is greater than 0, if not prompt the user to enter a valid number
             if sell_count > 0:
                noOfItems = sell_count
                break
             else: 
               
               print()
               print("Error: Please enter a valid number greater than 0.") 
               print()    
         except ValueError:
             # If user enters a non-numeric value, prompt the user to enter a numeric value
             print("+-----------------------------------------------------------------------------------------------+")
             print()
             print()
             print("Error: Please enter a numeric value.")
             
             print()


        for block in rd.datalist:
            for inner_element in block:
                if id_.lower() == inner_element.lower():
                    if sell_count>int(block[3]) or int(block[3])<= 0:
                         # If the item is out of stock or the entered sell count is greater than the available quantity, 
                         # prompt the user that the item is out of stock
                        print()
                        print("THE ITEM IS OUT OF STOCK!")
                        
                    else:
                        # If the entered sell count is valid and the item is in stock, display the available quantity
                        print()
                        print("+-----------------------------------------------------------------------------------------------+")
                        print("# Total Items Available In Stock--> ", block[3])
                        print("+-----------------------------------------------------------------------------------------------+")
                        print()

                        # Update the inventory by subtracting the sold quantity from the available quantity
                        rem_product = int(block[3]) - sell_count
                        block[3] = " "+str(rem_product)
                        print()
                        
                        sold_items=[]

                        sold_items=block[:] 
                        #dont mess with block as it is inside  datakist which is uded to update
                        sold_items.append(str(noOfItems))

                        multiple_sells.append(sold_items)

                        mul_sell=multiple_sells[:]

                        continue_=True
                        while continue_:
                            print("+-----------------------------------------------------------------------------------------------+")    
                            ans = input("Do you want to continue to sell Enter 'Y' for YES and 'N' for NO --> ")
                            print("+-----------------------------------------------------------------------------------------------+")
                            if ans.lower() == "n":
                                sell = False
                                continue_=False
                                print()
                                print()
                                print()
                            elif ans.lower() == "y": 
                                global issingleSell
                                sin_sell=False
                                issingleSell=sin_sell
                                continue_=False
                            else:
                                print()
                                print("Invalid Input!, Please Input Either 'y' or 'n' ")
                                print()
    while True: 
        print("+-----------------------------------------------------------------------------------------------+")                     
        confirm_=input("Do you want your item to be shipped ? Please Enter 'y' for yes and 'n' for NO --> ")
        print("+-----------------------------------------------------------------------------------------------+") 
        if confirm_=='y':
              global ship
              ship_=True
              ship=ship_
              print()
              print()
              print("\t\t\t+=========================================================================================================+")
              print("\t\t\t\t\t### THANK YOU! THE STOCK IS UPDATED AND SELL BILL IS GENERATED ###")
              print("\t\t\t+=========================================================================================================+")
              print("\t")
              print()
              break
        elif confirm_=='n':
              ship_=False
              ship=ship_
              print()
              print()
              print("\t\t\t+=========================================================================================================+")
              print("\t\t\t\t\t### THANK YOU! THE STOCK IS UPDATED AND SELL BILL IS GENERATED ###")
              print("\t\t\t+=========================================================================================================+")
              print("\t")
              print()
              break
        else:
            print()
            print()
            print("INVALID ! INPUT PLEASE INPUT 'y' or 'n'")
            print()
            print()

    wr.update()
    wr.sell_invoice()


#order product method
productname=""
brandname=""
processor=""
price=""
graphics=""
quantity=""
customername_ =""
issinleOrder=True
multiple_order=[]
def order_products():
  """
    This function allows the user to place an order for a laptop. It prompts the user to enter the product name, brand name,
    processor details, graphics details, price, and quantity of the laptop. The inputs are validated to ensure they meet
    certain criteria (e.g., the product name should not contain numeric values). Once the order is complete, the order
    information is stored in a list called multiple_order. The user can choose to continue ordering or end the ordering
    process. If the user ends the process, an order invoice is generated, and the order information is updated in the stock
    database. If the user chooses to continue ordering, the function calls the update_order() function to update the stock
    database with the current order information.

    Returns:
    None
    """
  order=True
  # Start inner while loop for input validation
  while order: 
        print()
        print("# Please Enter The Following INFORMATION OF LAPTOP TO PLACE ORDER --> \n")
        while True:
                global productname
                print()
                print("+-----------------------------------------------------------------------------------------------+") 
                Product_name = input("ENTER THE PRODUCT NAME: ")
                print("+-----------------------------------------------------------------------------------------------+") 
                print()
                # Check if input contains numeric values
                if not Product_name.isnumeric() and Product_name != "": # Check if input contains numeric values
                        productname = Product_name
                        # Break inner while loop if input is valid
                        break
                else:
                        print()
                        print("Invalid input! Product Name should not contain numeric values and Empty Values")
                        print()
                


        while True:
                    global brandname
                    print()
                    print("+-----------------------------------------------------------------------------------------------+") 
                    Brand_name = input("ENTER THE BRAND NAME: ")
                    print("+-----------------------------------------------------------------------------------------------+") 
                    print()
                    brandname = Brand_name
                    if not Brand_name.isnumeric() and Brand_name != "": # Check if input contains numeric values
                        brandname = Brand_name
                        break
                    else:
                        # Display error message if input is invalid and continue inner while loop
                        print()
                        print("Invalid input! Brand Name should not contain numeric values and Empty Values")
                        print()
                



        while True: # Infinite loop until valid input is entered
                global processor
                print()
                print("+-----------------------------------------------------------------------------------------------+") 
                PROCESSOR = input("ENTER THE PROCESSOR DETAILS: ")
                print("+-----------------------------------------------------------------------------------------------+") 
                print()
                if not PROCESSOR.isnumeric() and PROCESSOR != "": # Check if input contains numeric values
                        processor = PROCESSOR # Store valid input in global variable 'processor'
                        break # Exit loop
                else:
                        print()
                        print("Invalid input! Processor Name should not contain numeric values and Empty Values")
                        print()
        

                

        while True:
            try:
                global price

                print()
                print("+-----------------------------------------------------------------------------------------------+") 
                PRICE = int(input("ENTER THE PRICE OF THE PRODUCT: ")) 
                print("+-----------------------------------------------------------------------------------------------+") 
                print()
                if PRICE > 0: # check if price is a positive number
                        price = PRICE
                        break
                    
                else: 
                    print()
                    print("Error: Please enter a valid Price")
                    print()
                    
            except ValueError:
                    
                    print("+-----------------------------------------------------------------------------------------------+") 
                    print()
                    print()
                    print("Invalid input! Please enter a numeric value for PRICE.") # if input is not a number, display error message
                    print()


        # This loop prompts the user to enter the graphics details of the laptop and validates the input
        while True:
                global graphics # Declare the 'graphics' variable as global so it can be accessed outside the loop
                print()
                print("+-----------------------------------------------------------------------------------------------+") 
                GRAPHICS = input("ENTER THE GRAPHICS DETAILS: ")
                print("+-----------------------------------------------------------------------------------------------+") 
                print()
                if not GRAPHICS.isnumeric() and GRAPHICS != "": # Check if input contains numeric values
                        graphics = GRAPHICS # Assign the valid input to the 'graphics' variable and break out of the loop
                        break
                else:
                        print()
                        print("Invalid input! Graphics should not contain numeric values and Empty Values")
                        print()
        
        

        
        while True:
            try:
                global quantity
                print()
                print("+-----------------------------------------------------------------------------------------------+") 
                Quantity = int(input("ENTER THE NO OF QUANTITY: ")) # Convert input to integer
                print("+-----------------------------------------------------------------------------------------------+") 
                print()
                if Quantity > 0: # Check if quantity is greater than 0
                        quantity = Quantity # Set the value of quantity to the user input
                        break # Exit the loop
                else: 
                    print()
                    print("Error: Please enter a valid number greater than 0.") # If the quantity entered is 0 or negative, print an error message and prompt the user to enter a valid number

                    print()
            except ValueError: # If the user input cannot be converted to an integer, catch the ValueError and print an error message
                print("+-----------------------------------------------------------------------------------------------+") 
                print()
                print()
                print("Invalid input! Please enter an integer value for QUANTITY.")
                print()



        order_items=[productname, brandname, price, quantity, processor, graphics]
        multiple_order.append(order_items)
        continue_=True
        while continue_:
                print()
                print("+-----------------------------------------------------------------------------------------------+")    
                ans = input("Do you want to continue to ORDER Enter 'Y' for YES and 'N' for NO --> ")
                print("+-----------------------------------------------------------------------------------------------+")
                print()
                
                if ans.lower() == "n":
                    order = False
                    continue_=False
                    print()
                    print()
                    print("\t\t\t     +=============================================================================================================+")
                    print("\t\t\t\t        ### THANK YOU! ORDER IS PLACED THE STOCK IS UPDATED AND ORDER BILL IS GENERATED ###")
                    print("\t\t\t     +=============================================================================================================+")
                    print("\n")
                    print()
                elif ans.lower() == "y": 
                    global issinleOrder
                    sin_order=False
                    issinleOrder=sin_order
                    continue_=False
                    wr.udpate_order()
                else:
                    print()
                    print("Invalid Input!, Please Input Either 'y' or 'n' ")
                    print()


  wr.order_invoice()
  wr.udpate_order()

def username():
     """
    This function prompts the user to input a customer name and checks if the input contains numeric values.
    If the input is valid, it sets the global variable customername_ to the input value and returns nothing.
    If the input is invalid, it displays an error message and prompts the user to input again.

    Returns:
    None
    """
     while True:
                print()
                print("+-----------------------------------------------------------------------------------------------+")
                customername = input(">> Enter the CUSTOMER NAME: ")
                print("+-----------------------------------------------------------------------------------------------+")
                print()
                if not customername.isnumeric() and customername != "":# Check if input contains numeric values
                    global customername_
                    customername_ = customername
                    break
                else:
                     print()
                     print("Invalid input! Customer Name should not contain numeric values and Empty Values")
                     print()
           
def screen_display_Sorder():
      
      """
     Prints an order invoice for a laptop purchase, including distributor name, laptop name, brand name,
     , graphics card, quantity, net price, VAT amount, date and time of order, and gross amount.

     Returns:
     None
      """
      netamt=(int(price)*int(quantity))
      vatamt=(int(price)*0.13)*int(quantity)
      grossamt=netamt+vatamt
     
      head1="""                                  +======================================================================================================+
                                  |                            #----- Miraj Laptop and Computer Shop -----#                              |
                                  |                                                                                                      |
                                  |                                        Kalanki-14, Kathmandu                                         |
                                  |                                                                                                      |
                                  |                               Contact Number:- 9844345562 , 01-43567800                              |
                                  |                                                                                                      |
                                  +======================================================================================================+
                                  |                                                                                                      |
                                  | --------------------------------------------ORDER INVOICE -------------------------------------------|"""
      
      data1="""
                                  |                                                                                                      |
                                    >> DISTRIBUTOR NAME:                                           {}                       
                                  |                                                                                                      |
                                    >> LAPTOP NAME:                                                            {}                       
                                  |                                                                                                      |
                                    >> BRAND NAME:                                                             {}                       
                                  |                                                                                                      |
                                    >> PROCESSOR:                                                              {}                       
                                  |                                                                                                      |
                                    >> GRAPHICS CARD:                                                          {}                       
                                  |                                                                                                      |
                                    >> QUANTITY:                                                               {}                       
                                  |                                                                                                      |
                                    >> NET PRICE:                                                              {}                       
                                  |                                                                                                      |
                                    >> VAT AMOUNT:                                                             {}                        
                                  |                                                                                                      |                   
                                    >> DATE OF ORDER:                                                          {}                                                                                                                          
                                  |                                                                                                      |
                                    >> TIME OF ORDER:                                                          {}                         
                                  |______________________________________________________________________________________________________|
                                  |                                                                                                      |
                                    >> GROSS AMOUNT:                                                           {}                       
                                  |______________________________________________________________________________________________________|""".format("Miraj Laptop and Computer Shop", productname, brandname, processor, graphics, quantity, "$ "+str(netamt), "$ "+str(vatamt), wr.now.date(), wr.now.time(),"$ "+str(grossamt))
     
      foot1="""
                                  |                                                                                                      |
                                  |--------------------------- THANK YOU! We hope to see you again soon! --------------------------------|
                                  |                                                                                                      |
                                  +======================================================================================================+
                              """  
      print(head1)
      print(data1)
      print(foot1)

def screen_display_Morder():
                 """
                  Displays the multiple orders in a tabular format with details such as laptop name, brand name, total amount, 
                  VAT amount, total amount with VAT, quantity purchased, processor, and graphics card. It also calculates and 
                  displays the total amount, total VAT, amount with VAT, and the total number of items purchased.

                  Returns:
                  None
                 """
                 header = "+{}+\n".format("=" * 171)
                 table_header = "| {:>20} | {:>15} | {:>12} | {:>15} | {:>29} | {:>20} | {:>15} | {:>22} |\n".format("LAPTOP NAME", "BRAND NAME", "TOTAL AMOUNT", "VAT AMOUNT", "TOTAL AMOUNT WITH VAT", "QUANTITY PURCHASED", "PROCESSOR", "GRAPHICS CARD")
                 name= "|{:^171}|\n".format("#----- Miraj Laptop and Computer Shop -----#")
                 address="|{:^171}|\n".format("Kalanki-14 , Kathmandu")
                 cont="|{:^171}|\n".format("Contact Number:- 9844345562 , 01-43567800")
                 space="+{}+\n".format(" " * 171)
                 dots="+{}+\n".format("-" * 171)
                 rdots="+{}+\n".format("." * 171)
                 distributorname="| Distributor Name: {:<25}                                                                                                                          |\n".format("Miraj Laptop and Computer Shop")
                 Date="| Date of Purchase: {}                                                                                                                                              |\n".format(wr.now.date())
                 Time="| Time of Purchase: {}                                                                                                                                         |\n".format(wr.now.time())
                 greet= "|{:^171}|\n".format("#----- THANK YOU! We hope to see you again soon! -----#")

                 print(header)
                 print(name)
                 print(space)
                 print(address)
                 print(space)
                 print(cont)
                 print(dots)
                 print(distributorname)
                 print(Date)
                 print(Time)
                 print(header)   
                 print(table_header)
                 print(header) 

                 total_amount=0
                 total_vat=0
                 amount_with_vat=0
                 t_items=0

                 for i in multiple_order:
                     
                            total_amount += int(i[2])* int(i[3])
                            total_vat +=(0.13* int(i[2])* int(i[3]))
                            amount_with_vat+=(float(i[2])+float(0.13* int(i[2])))* int(i[3])
                            t_items += int(i[3])
                            
                            
                            print("| {:>20} | {:>15} | {:>12} | {:>15.2f} | {:>29.2f} | {:>20} | {:>15} | {:>22} |\n".format(i[0], i[1], "$" + str(i[2] * int(i[3])), (0.13 * int(i[2])) * int(i[3]), (int(i[2]) + (0.13 * int(i[2]))) * int(i[3]), str(i[3]), i[4], i[5]))

                
                #outside loop
                 print(header)    
                 total_bar= "  TOTAL:                                 | {:<12} | {:<15} | {:<29} | {:<20} |\n".format("${:.2f}".format(total_amount), "${:.2f}".format(total_vat), "${:.2f}".format(amount_with_vat), t_items)
                 print(total_bar) 
                 print(rdots)
                 print(greet)
                 print(header)