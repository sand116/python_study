import unittest 
from customer import Customer
 
class TestCustomers(unittest.TestCase): 
    def test_making_customer(self):
        name = '최명규'
        address = '대치동'
        is_contracted = True
        is_enabled = False
 
        customer = Customer(name, address, is_contracted, is_enabled)
 
        self.assertEqual(customer.name, name)
        self.assertEqual(customer.address, address)
        self.assertEqual(customer.is_contract, is_contracted)
        self.assertEqual(customer.is_enabled, is_enabled)

if __name__ == '__main__':
    unittest.main()