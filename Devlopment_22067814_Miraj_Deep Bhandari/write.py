#import required modules
import datetime
import operation as op
import read as rd


now = datetime.datetime.now()
#sell invoice generator method
def sell_invoice():
    """
    This function generates a sell invoice in a text file format for a single sell or multiple sells 
    made by the user.

    For a single sell, the function extracts relevant information from the `op` object and `rd.datalist`
    and generates a bill with the customer name, laptop name, brand name, date and time of purchase, 
    total amount, shipping cost (if shipping is chosen), and total amount including shipping cost.

    For multiple sells, the function creates a table of laptop names, brand names, total amounts, shipping 
    costs, total amounts with shipping costs, and quantity purchased, and calculates the grand total.

    The function saves the generated invoice in a text file format in a folder named "Sell_Invoices"
    located in the current working directory.

    Parameters:
    None

    Returns:
    None
    """

    year_str = str(now.year)
    month_str = str(now.month)
    day_str = str(now.day)
    hour_str = str(now.hour)
    minute_str = str(now.minute)
    second_str = str(now.second)
    date_and_time_str = year_str + month_str + day_str + hour_str + minute_str + second_str


    base_filename = f"{op.customername_}_{date_and_time_str}_Sell_Invoice.txt"
    
    path1 = r".\Sell_Invoices\{}".format(base_filename)
    
    # Open the file at the specified path in write mode, overwriting any existing contents
    with open(path1, "w") as invoice:
         # Check whether the current transaction is for a single item
         if  op.issingleSell: 
              # Iterate through the list of data blocks    
              for block in rd.datalist:
                  # Iterate through the elements in the current data block
                  for inner_element in block:
                       # Check whether the current element matches the ID of the current transaction
                      if op.id_.lower() == inner_element.lower():
                          # Store the current data block as the invoice info
                          invoice_info_list = block
                          # Calculate the shipping amount if shipping is required
                          if op.ship==True:
                             # The shipping amount is 25% of the item price, multiplied by the number of items
                             shippingamt = (0.25 * int(block[2][2:])) * op.noOfItems 
                             # Calculate the total amount including shipping
                             total_amt_withshipping = shippingamt + (int(block[2][2:])) * (op.noOfItems)
                          # If shipping is not required, set the shipping amount to 0
                          # and calculate the total amount without shipping
                          elif op.ship==False:
                              shippingamt = 0
                              total_amt_withshipping = shippingamt + (int(block[2][2:])) * (op.noOfItems)
                              


                          head="""                          +======================================================================================================+
                          |                            #----- Miraj Laptop and Computer Shop -----#                              |
                          |                                                                                                      |
                          |                                        Kalanki-14, Kathmandu                                         |
                          |                                                                                                      |
                          |                                Contact Number:- 9844345562 , 01-43567800                             |
                          |                                                                                                      |
                          +======================================================================================================+
                          |                                                                                                      |
                          | --------------------------------------------SELL INVOICE --------------------------------------------|"""

                          data="""
                          |                                                                                                      |
                            >> CUSTOMER NAME:                                                           {}                       
                          |                                                                                                      |
                            >> LAPTOP NAME:                                                             {}                       
                          |                                                                                                      |
                            >> BRAND NAME:                                                             {}                       
                          |                                                                                                      |
                            >> DATE OF PURCHASE:                                                        {}                       
                          |                                                                                                      |
                            >> TIME OF PURCHASE:                                                        {}                       
                          |                                                                                                      |
                            >> TOTAL AMOUNT EXCLUDING SHIPPING COST:                                    {}                       
                          |                                                                                                      |
                            >> SHIPPING COST:                                                           {}                       
                          |                                                                                                      |
                                                                                                                                
                          |______________________________________________________________________________________________________|
                          |                                                                                                      |
                            >> TOTAL AMOUNT INCLUDING SHIPPING COST:                                    {}                       
                          |______________________________________________________________________________________________________|""".format( op.customername_, invoice_info_list[0], invoice_info_list[1], now.date(), now.time(),"$ "+str((int(invoice_info_list[2][2:])) * op.noOfItems), "$ "+str(shippingamt), "$ "+str(total_amt_withshipping))

                          foot="""
                          |                                                                                                      |
                          |--------------------------- THANK YOU! We hope to see you again soon! --------------------------------|
                          |                                                                                                      |
                          +======================================================================================================+
                      """  
                          invoice.write(head) 
                          invoice.write(data) 
                          invoice.write(foot)
                          print(head) 
                          print(data) 
                          print(foot)  

         else:
          
            header = "+{}+\n".format("=" * 150)
            table_header = "| {:>27} | {:>23} | {:>14} | {:>17} | {:>32} | {:>20} |\n".format("LAPTOP NAME", "BRAND NAME", "TOTAL AMOUNT", "SHIPPING COST", "TOTAL AMOUNT WITH SHIPPING COST", "QUANTITY PURCHASED")
            name= "|{:^150}|\n".format("#----- Miraj Laptop and Computer Shop -----#")
            address="|{:^150}|\n".format("Kalanki-14 , Kathmandu")
            space="+{}+\n".format(" " * 150)
            cont="|{:^150}|\n".format("Contact Number:- 9844345562 , 01-43567800")
            dots="+{}+\n".format("-" * 150)
            rdots="+{}+\n".format("." * 150)
            Customername="| Customer Name: {:<25}                                                                                                             |\n".format(op.customername_)
            Date="| Date of Purchase: {}                                                                                                                         |\n".format(now.date())
            Time="| Time of Purchase: {}                                                                                                                    |\n".format(now.time())
            greet= "|{:^150}|\n".format("#----- THANK YOU! We hope to see you again soon! -----#")

            #writing in invoive
            invoice.write(header)
            invoice.write(name)
            invoice.write(space)
            invoice.write(address)
            invoice.write(space)
            invoice.write(cont)
            invoice.write(space)
            invoice.write(dots)
            invoice.write(Customername)
            invoice.write(Date)
            invoice.write(Time)
            invoice.write(header)   
            invoice.write(table_header)  
            invoice.write(header)
            invoice.write(header)

           #print bill on screen 
            print(header)
            print(name)
            print(space)
            print(address)
            print(space)
            print(cont)
            print(space)
            print(dots)
            print(Customername)
            print(Date)
            print(Time)
            print(header)   
            print(table_header)  
            print(header)
            print(header)


            total_amount=0
            total_shipping=0
            amount_with_shipping=0
            t_items=0
            
          
            for i in op.mul_sell:
                 
                 # Calculate the total amount by multiplying the item price by the quantity and adding it to the existing total amount
                 total_amount += int(i[2][2:])* int(i[7])
                 # Calculate the total shipping cost by multiplying the item price by 0.25 and the quantity, and adding it to the existing total shipping cost
                 total_shipping +=(0.25* int(i[2][2:])* int(i[7]))
                 # If shipping is required, calculate the total amount including shipping
                 if op.ship==True:
                    # Calculate the item price plus 25% of the item price, multiplied by the quantity, and add it to the existing amount with shipping
                    amount_with_shipping+=(float(i[2][2:])+float(0.25* int(i[2][2:])))* int(i[7])
                 # If shipping is not required, calculate the total amount without shipping
                 elif op.ship==False:
                      # Calculate the item price multiplied by the quantity, and add it to the existing amount with shipping
                     amount_with_shipping+=(float(i[2][2:]))* int(i[7])
                 

                 t_items += int(i[7])
                 if op.ship==True:
                        invoice.write("| {:<27} | {:<23} | {:<14} | {:<17} | {:<32} | {:<20} |\n".format(i[0], i[1], "$"+str(int(i[2][2:])* int(i[7])), ("$"+str(0.25* int(i[2][2:])* int(i[7]))), "$"+str((float(i[2][2:])+float(0.25* int(i[2][2:])))* int(i[7])),i[7]  ))
                        #for print in screen
                        print("| {:<27} | {:<23} | {:<14} | {:<17} | {:<32} | {:<20} |\n".format(i[0], i[1], "$"+str(int(i[2][2:])* int(i[7])), ("$"+str(0.25* int(i[2][2:])* int(i[7]))), "$"+str((float(i[2][2:])+float(0.25* int(i[2][2:])))* int(i[7])),i[7]  ))
                 elif op.ship==False:
                      invoice.write("| {:<27} | {:<23} | {:<14} | {:<17} | {:<32} | {:<20} |\n".format(i[0], i[1], "$"+str(int(i[2][2:])* int(i[7])), ("$"+str(0)), "$"+str((float(i[2][2:]))* int(i[7])),i[7]  ))
                         #for print in screen
                      print("| {:<27} | {:<23} | {:<14} | {:<17} | {:<32} | {:<20} |\n".format(i[0], i[1], "$"+str(int(i[2][2:])* int(i[7])), ("$"+str(0)), "$"+str((float(i[2][2:]))* int(i[7])),i[7]  ))
                  
                     

          #outside the loop

            invoice.write(header)
            if op.ship==True:
               total_bar="|  TOTAL:                                               | {:<15} | {:<16} | {:<32} | {:<20} |\n".format("$"+str(total_amount),"$"+str(total_shipping),"$"+str(amount_with_shipping), t_items)
            elif op.ship==False:
               total_bar="|  TOTAL:                                               | {:<15} | {:<16} | {:<32} | {:<20} |\n".format("$"+str(total_amount),"$"+str(0),"$"+str(amount_with_shipping), t_items)
                
                
            invoice.write(total_bar)
            invoice.write(rdots)
            invoice.write(greet)
            invoice.write(header)
           
           #to print in screen
            print(header)
            print(total_bar)
            print(rdots)
            print(greet)
            print(header)

            




# data update method after sell
def update():
    """
    Writes the contents of `rd.datalist` to the file specified by `rd.path`. 
     
    For each block in `rd.datalist`, the elements are joined together with a comma
    separator and written to the file. Each block is written on a new line in the
    file.
    
    At summary this function is used to update the quantity of the products after sell at txt file

    Args:
        None

    Returns:
        None
    """
    with open(rd.path, 'w') as file:
       for block in rd.datalist: #for each loop
          para=",".join(block)
          file.write(para+"\n")




#order invoice generator method
def order_invoice():
    
      """
      This function generates an order invoice for a given order.

      The order invoice includes the following information:
      - Distributor name
      - Contact information
      - Laptop and brand name
      - Processor and graphics card
      - Quantity of the product
      - Net price
      - VAT amount
      - Gross amount
      - Date and time of order

      The function first generates a unique filename for the invoice, based on the current date and time, and saves it in
      the 'Order_Invoices' folder in the current directory. It then calculates the net amount, VAT amount, and gross
      amount of the order. Finally, it writes the invoice information to the file.

      If the order is a single order, the invoice includes only information for that order. If it is a multiple order, the
      invoice includes a table of information for each product in the order.

      return: None
    """
      year_str = str(now.year)
      month_str = str(now.month)
      day_str = str(now.day) 
      hour_str = str(now.hour)
      minute_str = str(now.minute)
      second_str = str(now.second)
      date_and_time_str = year_str + month_str + day_str + hour_str + minute_str + second_str


      base_filename = f"{op.productname}_{date_and_time_str}_Order_Invoice.txt"
            
     
      path2 = r".\Order_Invoices\{}".format(base_filename)
    
      # Calculate the net amount by multiplying the item price by the quantity
      netamt=(int(op.price)*int(op.quantity))
      # Calculate the VAT amount by multiplying the item price by 0.13 and the quantity
      vatamt=(int(op.price)*0.13)*int(op.quantity)
      # Calculate the gross amount by adding the net amount and the VAT amount
      grossamt=netamt+vatamt

     
      with open(path2,"w") as orderInvoice:
                  
           if op.issinleOrder:
                 
                  head1="""                                  +======================================================================================================+
                                  |                            #----- Miraj Laptop and Computer Shop -----#                              |
                                  |                                                                                                      |
                                  |                                        Kalanki-14, Kathmandu                                         |
                                  |                                                                                                      |
                                  |                                Contact Number:- 9844345562 , 01-43567800                             |
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
                                  |______________________________________________________________________________________________________|""".format("Miraj Laptop and Computer Shop", op.productname, op.brandname, op.processor, op.graphics, op.quantity, "$ "+str(netamt), "$ "+str(vatamt), now.date(), now.time(),"$ "+str(grossamt))
                  foot1="""
                                  |                                                                                                      |
                                  |--------------------------- THANK YOU! We hope to see you again soon! --------------------------------|
                                  |                                                                                                      |
                                  +======================================================================================================+
                              """  
                  
                
                  orderInvoice.write(head1)
                  orderInvoice.write(data1)
                  orderInvoice.write(foot1)
                  op.screen_display_Sorder()
                 
           
           else:
                 header = "+{}+\n".format("=" * 171)
                 table_header = "| {:>20} | {:>15} | {:>12} | {:>15} | {:>29} | {:>20} | {:>15} | {:>22} |\n".format("LAPTOP NAME", "BRAND NAME", "TOTAL AMOUNT", "VAT AMOUNT", "TOTAL AMOUNT WITH VAT", "QUANTITY PURCHASED", "PROCESSOR", "GRAPHICS CARD")
                 name= "|{:^171}|\n".format("#----- Miraj Laptop and Computer Shop -----#")
                 address="|{:^171}|\n".format("Kalanki-14 , Kathmandu")
                 cont="|{:^171}|\n".format("Contact Number:- 9844345562 , 01-43567800")
                 space="+{}+\n".format(" " * 171)
                 dots="+{}+\n".format("-" * 171)
                 rdots="+{}+\n".format("." * 171)
                 distributorname="| Distributor Name: {:<25}                                                                                                                          |\n".format("Miraj Laptop and Computer Shop")
                 Date="| Date of Purchase: {}                                                                                                                                              |\n".format(now.date())
                 Time="| Time of Purchase: {}                                                                                                                                         |\n".format(now.time())
                 greet= "|{:^171}|\n".format("#----- THANK YOU! We hope to see you again soon! -----#")
                 
                 orderInvoice.write(header)
                 orderInvoice.write(name)
                 orderInvoice.write(space)
                 orderInvoice.write(address)
                 orderInvoice.write(space)
                 orderInvoice.write(cont)
                 orderInvoice.write(dots)
                 orderInvoice.write(distributorname)
                 orderInvoice.write(Date)
                 orderInvoice.write(Time)
                 orderInvoice.write(header)   
                 orderInvoice.write(table_header)
                 orderInvoice.write(header)   

              
                

                 total_amount=0
                 total_vat=0
                 amount_with_vat=0
                 t_items=0

                 for i in op.multiple_order:
                    
                    # Calculate the total amount by multiplying the item price by the quantity and adding it to the existing total amount
                    total_amount += int(i[2])* int(i[3])
                    # Calculate the total VAT cost by multiplying the item price by 0.13 and the quantity, and adding it to the existing total VAT cost
                    total_vat +=(0.13* int(i[2])* int(i[3]))
                    # Calculate the total amount including VAT by adding the item price plus 13% of the item price, multiplied by the quantity, to the existing amount with VAT
                    amount_with_vat+=(float(i[2])+float(0.13* int(i[2])))* int(i[3])
                    # Add the quantity to the existing total number of items
                    t_items += int(i[3])
                     
                    orderInvoice.write("| {:>20} | {:>15} | {:>12} | {:>15.2f} | {:>29.2f} | {:>20} | {:>15} | {:>22} |\n".format(i[0], i[1], "$" + str(i[2] * int(i[3])), (0.13 * int(i[2])) * int(i[3]), (int(i[2]) + (0.13 * int(i[2]))) * int(i[3]), str(i[3]), i[4], i[5]))
                   

                #outside loop print
                 orderInvoice.write(header)    
                 total_bar = "  TOTAL:                                 | {:<12} | {:<15} | {:<29} | {:<20} |\n".format("${:.2f}".format(total_amount), "${:.2f}".format(total_vat), "${:.2f}".format(amount_with_vat), t_items)

                 orderInvoice.write(total_bar) 
                 orderInvoice.write(rdots)
                 orderInvoice.write(greet)
                 orderInvoice.write(header)
                 op.screen_display_Morder()

              



#order update method
def udpate_order():
        """
      Updates the order list with new items or increases the quantity of an existing item.

      - Finds the latest ID number from the order list and increments it to generate a new ID for the new item.
      - Searches the order list for an existing item with the same product name, brand name, processor, and graphics as the new item.
      - If found, updates the quantity of the existing item with the new quantity.
      - If not found, creates a new item with a new ID and adds it to the order list.
      - Saves the updated order list to the data file and reloads it into the data list.

      Returns:
      None
    """
        # Get the ID number of the last item in the data list, and increment it by 1 to generate a new ID number
        ID_num=rd.datalist[-1][-1]
        id_num=int(ID_num.replace("L","").strip())+1
    
        # Iterate through each list in the data list
        for eachlist in rd.datalist:
          # Check if the product name, brand name, processor, and graphics match the input values
          if op.productname.strip().lower() in [item.strip().lower() for item in eachlist] and op.brandname.strip().lower() in [item.strip().lower() for item in eachlist] and op.processor.strip().lower() in [item.strip().lower() for item in eachlist] and op.graphics.strip().lower() in [item.strip().lower() for item in eachlist]:
                # If there is a match, update the quantity by adding the input quantity to the existing quantity
                upd_noofitems=int(eachlist[3])+int(op.quantity)
                eachlist[3]=" "+str(upd_noofitems)
                update()
                # Exit the loop since the item has been updated
                break
        # If there is no match, add a new order item to the end of the data list
        else: 
            new_orderitem=[op.productname," "+op.brandname," $"+str(op.price)," "+str(op.quantity)," "+op.processor," "+op.graphics,str(id_num)+"L"]
            with open(rd.path, 'a') as file:
                para=",".join( new_orderitem)
                file.write(para+"\n")


        '''data list ma suru ma value file bata load vayo hunxa tei vara paxi update vayeko value tesma aaudina tesko lagi
          hami ley update gareko file ko value lai feri data list ma pathaunu parxa which is done below  --> aba yo gare paxi display 
          method call garda updated sell value ne aauxa'''
        
        rd.datalist = [] # same as data_info

        with open(rd.path, 'r') as file:
          for line in file:
              line = line.strip().split(",")
              rd.datalist.append(line)