import unittest
from pdf import PdfReport
from flat import Bill, Flatmate


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.bill = Bill(120, "March 2020")
        self.john = Flatmate('John', 20)
        self.marry = Flatmate('Marry', 25)

    def test_pay_both_flatmates_equal_total_bill(self):
        self.assertEqual(self.john.pays(self.bill, self.marry) + self.marry.pays(self.bill, self.john), self.bill.amount )  # add assertion here

    def test_pays_proportional_number_of_days(self):
        total_days_in_house = self.john.days_in_house + self.marry.days_in_house
        john_pays_coef = self.john.days_in_house / total_days_in_house

        print("actual: ", self.john.pays(self.bill, self.marry))
        print("expected: ", round(self.bill.amount * john_pays_coef, 2))

        self.assertEqual(self.john.pays(self.bill, self.marry), round(self.bill.amount * john_pays_coef, 2))


if __name__ == '__main__':
    unittest.main()
