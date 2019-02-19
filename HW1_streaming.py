##homework 1 sjf374 sam falk 02/11/2019
import csv
import sys

# if you add more than one word as argument it will give you an error as well--from class
if not len(sys.argv) == 3:
    print("Invalid number of arguments. Run as: python HW1_streaming.py <INPUT_CSV> <OUTPUT_CSV>")
    sys.exit()

##Takes in two file names
if __name__=='__main__':
        filename = sys.argv[1]
        filename_out = sys.argv[2]

    
def csvRows(filename):
    """
    Function to load each row and be able to call columns by dict functionality
    """
    with open(filename, 'r') as fi:
        reader = csv.DictReader(fi)
        for row in reader:
            yield(row)

sales = {}
for row in csvRows(filename):
    #current row important information
    product = row.get('Product ID')
    current_customer = row.get('Customer ID', 0)
    #create key where the product hasn't been saved as a key 
    if sales.get(product, -1) == -1:
        sales[product] = {}
    #add incremental value to the Revenue
    sales[product]['Total Revenue'] = float(row.get('Item Cost', 0))+ \
        sales[product].get('Total Revenue', 0)
    #since the input csv is sorted by customer 
    #only necessary to count a customer once per product purchased
    if sales[product].get('Last Customer', -1) != current_customer:
        sales[product]['Last Customer'] = current_customer
        sales[product]['CustCount'] = sales[product].get('CustCount', 0) + 1

#write the content of sales dictionary to file out
f_out = open(filename_out , 'w')
header = 'Product ID, Customer Count, Total Revenue\n'
f_out.write(header)
for k in sales:
    line = k + ', '+ str(sales[k].get('CustCount')) + ', '+ \
                     str(round(sales[k].get('Total Revenue'), 2)) + '\n'
    f_out.write(line)
