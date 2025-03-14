from fpdf import FPDF
from space_tracer.mock_turtle import color_map

pdf = FPDF(orientation='P',unit='pt',format='a4')
pdf.add_page()


#Add some text
pdf.set_font(family='times',style='B',size=24)
pdf.cell(w=0,h=80,txt="Flatmates Bill",border=0,align="C", ln=1)
pdf.cell(w=200,h=40,txt="Period",border=1, align="C")
pdf.cell(w=200,h=40,txt="March 2025",border=1, align="C")

pdf.output("Bill.pdf")