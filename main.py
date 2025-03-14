from Flat import Bill, Flatmate
from Reports import PdfReport

#Taking input from the User
Total_amount = float(input("Hey User, Enter the  Total Bill Amount: \n"))
Name_1 = input("What is your Name: \n")
Days_1 = int(input(f"How many days did {Name_1} stayed in the house during the bill period: \n"))
Name_2 = input("What is your Friend's Name: \n")
Days_2 = int(input(f"How many days did {Name_2} stayed in the house during the bill period: \n"))
Timeline = input(" Enter the period. e.g. March 2025): \n ")
# print(f"The Number Days both {Name_1} and {Name_2} stayed in  for the {Timeline} \n")


the_bill= Bill(amount=Total_amount, period=Timeline)
Friend_1 = Flatmate(name=Name_1, days_in_house=Days_1)
Friend_2 = Flatmate(name=Name_2, days_in_house=Days_2)

print(f"{Name_1} has to pay: ",Friend_1.pays(bill=the_bill, flatmate2=Friend_2))
print(f"{Name_2} has to pay: ",Friend_2.pays(bill=the_bill, flatmate2=Friend_1))

pdf_report = PdfReport(filename="Report1.pdf")
pdf_report.generate(flatmate1=Friend_1, flatmate2=Friend_2, bill=the_bill)
