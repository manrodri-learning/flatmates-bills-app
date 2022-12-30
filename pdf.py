import os
import webbrowser

from fpdf import FPDF

from flat import Flatmate, Bill


class PdfReport:
    """
    Creates a pdf report file that contains data about the flatmates such as
    the names, bill share amount,...
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1: Flatmate, flatmate2: Flatmate, bill: Bill):
        pdf = FPDF(orientation='P', format='A4', unit='pt')
        pdf.add_page()

        # Add image
        pdf.image("resources/house.png", w=30, h=30)

        # Insert Title
        pdf.set_font(
            family='Times',
            size=24,
            style='B'
        )

        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=0, align='C', ln=1)

        pdf.set_font(
            family='Times',
            size=14,
            style='B'
        )
        pdf.cell(w=100, h=40, txt="Period:", border=0, align='L')
        pdf.cell(w=150, h=40, txt=bill.period, align='L', border=0, ln=1)

        # Insert amount to pay for each flatmate
        pdf.set_font(
            family='Times',
            size=12,
        )

        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=100, h=25, txt=str(flatmate1.pays(bill, flatmate2)), border=0, ln=1)
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=100, h=25, txt=str(flatmate2.pays(bill, flatmate1)), border=0, ln=1)

        pdf.output(self.filename)
        current_dir = os.path.abspath(os.getcwd())
        report_path = os.path.join(current_dir, self.filename)
        webbrowser.open(f"file://{report_path}")
