import os
from fpdf import FPDF
import webbrowser


class Bill:
    """
    Object that contains data about a bill such as total amount and period of the bill
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Creates a flatmate person who lives in the class and pays a share of the bill
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill: Bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        return str(round(bill.amount * weight, 2))


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
        pdf.image("house.png", w=30, h=30)

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
        pdf.cell(w=100, h=25, txt=flatmate1.pays(bill, flatmate2), border=0, ln=1)
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=100, h=25, txt=flatmate2.pays(bill, flatmate1), border=0, ln=1)

        pdf.output(self.filename)
        current_dir = os.path.abspath(os.getcwd())
        report_path = os.path.join(current_dir, self.filename)
        webbrowser.open(f"file://{report_path}")


if __name__ == "__main__":
    the_bill = Bill(120, "March 2022")
    john = Flatmate("John", days_in_house=20)
    marry = Flatmate("Marry", days_in_house=25)

    print(f"{john.name} pays {john.pays(the_bill, flatmate2=marry)}")
    print(f"{marry.name} pays {marry.pays(bill=the_bill, flatmate2=john)}")

    pdf_report = PdfReport("Report.pdf")
    pdf_report.generate(flatmate1=john, flatmate2=marry, bill=the_bill)
