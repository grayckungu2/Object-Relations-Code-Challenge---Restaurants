

import unittest
from lib.Review import Review
from lib.Customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer1 = Customer("lacie", "kui")
        self.customer2 = Customer("Jane", "mwangi")
        self.customer3 = Customer("kerry", "kemmy")
        self.review1 = Review(self.customer1, " LongHorn Steakhouse ", 2)
        self.review2 = Review(self.customer2, " Sonny's BBQ", 4)
        self.review3 = Review(self.customer3, " Olive Garden", 7)


    def test_given_name(self):
        self.assertEqual(self.customer1.given_name, "lacie")
        self.assertEqual(self.customer2.given_name, "Jane")

    def test_family_name(self):
        self.assertEqual(self.customer1.family_name, "kui")
        self.assertEqual(self.customer2.family_name, "mwangi")

    def test_full_name(self):
        self.assertEqual(self.customer1.full_name(), "lacie kui")
        self.assertEqual(self.customer2.full_name(), "Jane mwanngi")

    def test_all(self):
        self.assertEqual(Customer.all(), [self.customer1, self.customer2, self.customer3])

    def test_restaurants(self):
        self.assertEqual(self.customer1.restaurants(), [" LongHorn Steakhouse "])
        self.assertEqual(self.customer2.restaurants(), [" Florida's Fresh Grill"])
        self.assertEqual(self.customer3.restaurants(), [" LongHorn Steakhouse "])

    def test_add_review(self):
        self.customer1.add_review("Capri Restaurant ", 4)
        self.assertEqual(self.customer1.restaurants(), [" LongHorn Steakhouse ", "Pollo Tropical "])

    def test_num_reviews(self):
        self.assertEqual(self.customer1.num_reviews(), 1)
        self.assertEqual(self.customer2.num_reviews(), 1)
        self.assertEqual(self.customer3.num_reviews(), 1)

    def test_find_by_name(self):
        self.assertEqual(Customer.find_by_name("kerry kemmy"), self.customer1)
        self.assertEqual(Customer.find_by_name("Jane mwangi"), self.customer2)
        self.assertEqual(Customer.find_by_name("lacie kui"), self.customer3)
        self.assertEqual(Customer.find_by_name("shanz kare"), None)

    def test_find_all_by_given_name(self):
        self.assertEqual(Customer.find_all_by_given_name("lacie"), [self.customer1, self.customer3])
        self.assertEqual(Customer.find_all_by_given_name("Jane"), [self.customer2])
        self.assertEqual(Customer.find_all_by_given_name("shanz"), [])

if __name__ == '__main__':
    unittest.main() 