# Formula to calculate and project the total sales.
# 2/20/20
# CTI-110 P2T1 - Sales Prediction
# Robert Beard
#
# Get the projected total slaes.
total_sales= float(input('Enter the projected sales: '))

# Calculate the profit as a 23 precent of total sales.
profit = total_sales * 0.23

# Display the profit.
print('This is the $', format(profit, ',.2f'))
