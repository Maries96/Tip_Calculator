print("Welcome to the Tip Calculator")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))
tip_amount = round(total_bill * (tip_percentage / 100))
print("This is your tip amount:$", tip_amount)
total_bill_plus_tip = round(total_bill + tip_amount, 2)
each_person_pays = total_bill_plus_tip / number_of_people
print("Each person pays:$", each_person_pays)
