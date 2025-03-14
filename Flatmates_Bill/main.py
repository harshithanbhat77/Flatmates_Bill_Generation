from Flat import Bill, Flatmate
from Reports import PdfReport

#Taking input from the User
Total_amount = float(input("Hey User, Enter the  Total Bill Amount: \n"))

Name_1 = input("What is your Name: \n")
Days_1 = int(input(f"How many days did {Name_1} stayed in the house during the bill period: \n"))

Name_2 = input("What is your Friend's Name: \n")
Days_2 = int(input(f"How many days did {Name_2} stayed in the house during the bill period: \n"))

Timeline = input(" Enter the period. e.g. March 2025): \n ")

#Objecta are Created and functions are evoked
the_bill= Bill(amount=Total_amount, period=Timeline)
flatmate1 = Flatmate(name=Name_1, days_in_house=Days_1)
flatmate2 = Flatmate(name=Name_2, days_in_house=Days_2)

#Prints Output over Terminal
print(f"{Name_1} has to pay: ",flatmate1.pays(bill=the_bill, flatmate2=flatmate2))
print(f"{Name_2} has to pay: ",flatmate2.pays(bill=the_bill, flatmate2=flatmate1))

pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(flatmate1=flatmate1, flatmate2=flatmate2, bill=the_bill)
