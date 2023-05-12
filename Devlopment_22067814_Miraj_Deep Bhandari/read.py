# set the path to the file containing product information
path ="product_info.txt"

''' create an empty list to store the product information
    in the list named datalist  '''
datalist = []

# Read in each line of file and append to data list
with open(path, 'r') as file:
    for line in file:
        line = line.strip().split(",")
        datalist.append(line)

# define the display_products() function       
def display_products():
    """
        Display a formatted table of products, including their ID, name, brand, price, quantity, processor, and graphics.

        This function takes no arguments and uses the global variable `datalist`, which is assumed to be a list of lists
        where each inner list contains information about a product, in the following order: name, brand, price, quantity,
        processor, graphics, and ID.

        The table is printed to the console using the `print` function and includes a header row with column names, a line
        separator, and one row for each product, with data aligned in columns according to a predefined format string.
        
    """
    # print the header row
    print("|=========================================================================================================================|")
    print("| {:<8} | {:<24} | {:<19} | {:<10} | {:<15} | {:<15} | {:<10} |".format("ID", "Product", " Brand", " Price", " Quantity", " Processor", " Graphics"))

    
    print("|=========================================================================================================================|")
    # iterate over each product in the datalist and print its information in a formatted row
    for i in datalist:
        print("| {:<8} | {:<24} | {:<19} | {:<10} | {:<15} | {:<15} | {:<10} |".format(i[6],i[0], i[1], i[2], i[3], i[4], i[5]))
        print("|=========================================================================================================================|")