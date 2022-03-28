""" This is the Calculator Class"""
class Calculator:
    """ This is the default result property"""
    result = 0

    def instance_method(self):
        return 'instance method called', self

    def add(self, value_1):
        """ This is the add method"""
        self.result = self.result + value_1
        return self.result

    def subtract(self, value_1):
        """ This is the subtract method"""
        self.result = self.result - value_1
        return self.result
        
    def multiply(self, value_1, value_2):
        """ This is the subtract method"""
        self.result = Multiplication.multiply(value_1, value_2)
        return self.result

    def divide(self,value_1, value_2):
        """This is the divide method"""
        if (value_2 == 0):
            self.result = "Divide By Zero Error!"
        else:
            self.result = value_1/value_2
        return self.result

    def get_result(self):
        """ This is the get result method"""
        return self.result
