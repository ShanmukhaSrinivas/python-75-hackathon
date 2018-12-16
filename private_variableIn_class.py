#Class with a private variable

class Bank:
    def __init__(self):
        self.accno = 1001
        self.name = 'Ganesh'
        self.bal = 5000.0
        self.__loan = 1500000.00

    def display(self):
        print('Acc.No= ', self.accno)
        print('Name= ', self.name)
        print('Balance= ', self.bal)
        
b = Bank()
b.display()

print('Acc.No= ', self.accno)
print('Name= ', self.name)
print('Balance= ', self.bal)
print('Bank_Loan=', self._Bank__loan)
