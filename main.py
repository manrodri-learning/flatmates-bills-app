from flat import Bill, Flatmate
from pdf import PdfReport

if __name__ == "__main__":
    bill_amount = float(input("Hey user, enter the bill amount"))
    bill_period = input("What is the Bill period? [i.e. March 2020]")

    flatmate1_name = input('What is the flatmate1 name?')
    flatmate1_days_in_house = float(input("How many days did the flatmate1 stayed in the house in the billing period?"))

    flatmate2_name = input('What is the flatmate2 name?')
    flatmate2_days_in_house = float(input("How many days did the flatmate2 stayed in the house in the billing period?"))

    report_file_name = input("what name will the report have?")

    the_bill = Bill(bill_amount, bill_period)
    flatmate_1 = Flatmate(flatmate1_name, days_in_house=flatmate1_days_in_house)
    flatmate_2 = Flatmate(flatmate2_name, days_in_house=flatmate2_days_in_house)

    print(f"{flatmate_1.name} pays {flatmate_1.pays(the_bill, flatmate2=flatmate_2)}")
    print(f"{flatmate_2.name} pays {flatmate_2.pays(bill=the_bill, flatmate2=flatmate_1)}")

    pdf_report = PdfReport(report_file_name)
    pdf_report.generate(flatmate1=flatmate_1, flatmate2=flatmate_2, bill=the_bill)
