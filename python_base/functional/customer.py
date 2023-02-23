class Customer:
     
    def __init__(self, name, address, is_contracted, is_enabled):
        self._name = name
        self._address = address
        self._is_contract = is_contracted
        self._is_enable = is_enabled
 
    @property
    def name(self):
        return self._name
 
    @property
    def address(self):
        return self._address
 
    @property
    def is_contract(self):
        return self._is_contract
 
    @property
    def is_enabled(self):
        return self._is_enable

