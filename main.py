class Bill:
    """
    Object that contains the data about a bill,
    such as total amount and period of the bill
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Creates a flatmate person who lives in the flat
    and pys a share of the bill
    """
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight =  self.days_in_house/(self.days_in_house +flatmate2.days_in_house)
        pays_to = bill.amount * weight
        return  pays_to


class PdfReport:
    """
    Creates a pdf file that contains data about the flatmates such as
    their names, their due amounts and the period of the bill
    """

    def __init__(self,filename):
        self.filename=filename


    def generate(self, flatmate1, flatmate2, bill):
        pass


the_bill=Bill(amount=300, period="March 2025")
john = Flatmate(name="john", days_in_house=20)
marry = Flatmate(name="marry", days_in_house=25)

print("John has to pay: ",john.pays(bill=the_bill, flatmate2=marry))
print("Marry has to pay: ",marry.pays(bill=the_bill, flatmate2=john))