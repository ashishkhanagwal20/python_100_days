print("Welcome to the tip calculator")
bill = int(input("What was the total bill?\n$"))
persons = int(input("How many people to split the bill?\n"))
tip_percent = int(input(
    "What percentage tip would you like to give? 10,12, or 15?\n"))
totalBill = bill + (bill * (tip_percent/100))
billPerPerson = str(totalBill/persons)
print("Each person should pay: $ " + billPerPerson)