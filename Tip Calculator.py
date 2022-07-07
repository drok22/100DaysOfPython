# Tip Calculator

print("Welcome to the tip calculator.\n")
total_bill = input("What was the total bill?\n")
tip_percentage = input("What percentage tip would you like to give?\n")
num_of_diners = input("How many people are splitting the bill?\n")

bill_amount = float(total_bill) / int(num_of_diners)
tip_amount = bill_amount * float(tip_percentage) / 100
payment_amount = "{:.2f}".format(bill_amount + tip_amount)

print("Each person should pay: $" + payment_amount)