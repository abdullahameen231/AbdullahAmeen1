#Author Abdullah Ameen
# store the sales values
sales_values = []

# collect user inputs
while True:
    # sales value and input
    while True:
        try:
            sale_price = float(input("Enter a property sales value: "))
            
            # value should be positive and non-zero
            if sale_price > 0:
                break
            else:
                print(" enter a positive non-zero value.")
        except ValueError:
            print("Invalid input")

    # Add valid sale price to the list
    sales_values.append(sale_price)

    # Does the user wants to enter another value
    while True:
        another = input("Enter another value Y or N: ").strip().lower()
        
        if another == 'y':
            break
        elif another == 'n':
            # Leave the loop if user enters 'N' or 'n'
            break
        else:
            print("Invalid input")

    if another == 'n':
        break  # Leave the outer loop when user chooses 'n'

# Sort the list of sales values
sales_values.sort()

# Display each property value 
for i in range(len(sales_values)):
    print(f"Property {i+1} ${sales_values[i]:,.2f}")

# Display minimum sales value
minimum = sales_values[0]
print(f"\nMinimum: ${minimum:,.2f}")

# Display maximum sales value
maximum = sales_values[-1]
print(f"Maximum: ${maximum:,.2f}")

# Display the total sales value
total = sum(sales_values)
print(f"Total: ${total:,.2f}")

# Display the average sales value
average = total / len(sales_values)
print(f"Average: ${average:,.2f}")

# Calculate the median 
if len(sales_values) % 2 == 1:
    # If its odd take the middle value
    median = sales_values[len(sales_values) // 2]
else:
    # If its even average the two middle values
    median = (sales_values[len(sales_values) // 2 - 1] + sales_values[len(sales_values) // 2]) / 2

print(f"Median: ${median:,.2f}")

# The commission 
commission = total * 0.03
print(f"Commission: ${commission:,.2f}")
