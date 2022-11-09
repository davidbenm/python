print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people_to_split_the_bill = int(input("How many people to split the bill? "))
bill_per_person = (bill + bill*tip/100)/people_to_split_the_bill
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")
