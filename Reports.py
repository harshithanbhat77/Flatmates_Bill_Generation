import webbrowser

from fpdf import FPDF


class PdfReport:
    """
    Creates a pdf file that contains data about the flatmates such as
    their names, their due amounts and the period of the bill
    """

    def __init__(self,filename):
        self.filename=filename


    def generate(self, flatmate1, flatmate2, bill):

        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2) ,2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1) ,2))

        pdf = FPDF(orientation='P', unit='pt', format='a4')
        pdf.add_page()

        #Add Icon
        pdf.image("house.png", w=30, h=30)

        # Insert title
        pdf.set_font(family='times', style='B', size=24)
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)

        #Insert Period label And Value
        pdf.set_font(family='times', style='B', size=14)
        pdf.cell(w=100, h=40, txt="Period", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0,ln=1)

        #Insert Name And Due Amount of the first flatmate bill
        pdf.set_font(family='times', style='B', size=12)
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=40, txt=flatmate1_pay, border=0,ln=1)

        #Insert Name And Due Amount of the Second flatmate bill
        pdf.cell(w=100, h=40, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=40, txt=flatmate2_pay, border=0,ln=1)


        pdf.output(self.filename)

        #Automatically opens pdf file
        webbrowser.open(self.filename)
