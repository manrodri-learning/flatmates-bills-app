
## Title: 
Flatmates Bill

## Description:

An app that gets as input an amount of a bill for a particular period and the days the flatmate stayed in the house
for that period and return how much each flatmate has to pay.<br>

It also generates a PDF report stating:
  - the flatmates name
  - the amount each flatmate is due to pay
  - The billing period
  - the app logo

## Objects types (classes):

look at the description to find out classes neccessary. 

- bill 
  - amount is an attribute of a bill
  - period is an attribute of a bill

- flatmate
  - days_in_house is an attribute each flatmate
  - name 
  - pays(bill)

- PDFReport:
   - filename (path)
   - save()
   - create(flatmate1, flatmate2, bill)