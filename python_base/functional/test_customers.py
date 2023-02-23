import unittest
from unittest import TestCase 
from ex_customer import Customer
from ex_customers import Customers
from customers import CustomerName
from customers import CustomerAddress
class TestCustomers(TestCase):
    def setUp(self):
        enable = True
        disable = False
 
        enabled_customers = [
            Customer('최명규', '대치동', True, enable),
            Customer('김홍민', '대치동', True, enable),
            Customer('천준희', '신림동', True, enable),
        ]
 
        disabled_customers = [
            Customer('이명규', '대치동', True, disable),
            Customer('최홍민', '대치동', True, disable),
            Customer('김준희', '신림동', True, disable),
            Customer('황성현', '신림동', True, disable),
        ]
        
        self.customer_list = enabled_customers + disabled_customers
        self.customers = Customers(self.customer_list)
    
    def test_get_length(self):
        result_length = len(self.customers)
        expected_length = len(self.customer_list)
        self.assertEqual(result_length, expected_length)
        
    
    def test_get_enabled_customer_names(self):
        result_names = self.customers.get_enabled_customer_names()
        # map : iterable한 객체의 요소를 지정된 함수로 처리해주어 iterable한 맵 객체를 반환해줌 
        # filter : iterable한 객체의 요소에서 지정된 함수 값이 true인 값만 뽑아서 iterable한 필터 객체 반환
        expected_names = list(
            map(lambda x: x.name,
                filter(lambda x: x.is_enabled, self.customer_list))
        )
        
        self.assertCountEqual(result_names, expected_names)
    
    def test_get_enabled_customer_addresses(self):
        result_names = self.customers.get_enabled_customer_addresses()
        expected_names = list(
            map(lambda x: x.address,
                filter(lambda x: x.is_enabled, self.customer_list))
        )
        self.assertCountEqual(result_names, expected_names)





if __name__ == '__main__':
    unittest.main()




