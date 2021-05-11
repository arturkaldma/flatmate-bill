from flat import Bill, Flatmate
from reports import PdfReport

amount = float(input("Bill amount: "))
period = input("Bill period (E.g. April 2021): ")

name1 = input("Your name: ")
days_in_house1 = int(input(f"{name1} spent days: "))
name2 = input("Your roommate's name: ")
days_in_house2 = int(input(f"{name2} spent days: "))

the_bill = Bill(amount, period)
flatmate1 = Flatmate(name1, days_in_house1)
flatmate2 = Flatmate(name2, days_in_house2)

print(f"{name1} pays: ", flatmate1.pays(the_bill, flatmate2))
print(f"{name2} pays: ", flatmate2.pays(the_bill, flatmate1))

pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(flatmate1, flatmate2, the_bill)
