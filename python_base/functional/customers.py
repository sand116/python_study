#인터페이스 
class ConversionFunction:
     
    def call(self, customer):
        raise NotImplementedError

# 로직은 같지만, 다루는 정보가 다름

#이름 처리하는 함수
class CustomerName(ConversionFunction):
     
    def call(self, customer):
        return customer.name
# 주소 처리하는 함수 
class CustomerAddress(ConversionFunction):
     
    def call(self, customer):
        return customer.address


class Customers:
     
    def __init__(self, customers):
        self.customers = customers
    def __len__(self):
        return len(self.customers)
    '''
    def get_enabled_customer_names(self):
        ret_list = []
        for customer in self.customers:
            if customer.is_enabled:
                ret_list.append(customer.name)
        return ret_list
    
    def get_enabled_customer_addresses(self):
        ret_list = []
        for customer in self.customers:
            if customer.is_enabled:
                ret_list.append(customer.address)
        return ret_list
        
    로직 중복
    '''
    # 원하는 함수를 전달
    
    def get_enabled_customer_names(self):
            return self.get_enabled_customer_field(CustomerName())
 
    def get_enabled_customer_addresses(self):
        return self.get_enabled_customer_field(CustomerAddress())

    def get_enabled_customer_field(self, func):
        ''' 
            ret_list = []
            for customer in self.customers:
                if customer.is_enabled:
                    ret_list.append(func.call(customer))
            return ret_list
        '''
        enabled_customer = filter(lambda x: x.is_enabled, self.customers)
        return list(map(func.call, enabled_customer))








