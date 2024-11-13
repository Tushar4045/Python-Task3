class calci():
    def __init__(self,a=0,b=0,c=0,d=0,e=0):
        self.val1 = a
        self.val2 = b
        self.val3 = c
        self.val4 = d
        self.val5 = e

    def add(self):
        print('Addition: ',self.val1+self.val2+self.val3+self.val4+self.val5)

    def sub(self):
        print('Substraction: ',self.val1-self.val2-self.val3-self.val4-self.val5)

    def multi(self):
        print('Multiplication: ',self.val1*self.val2*self.val3*self.val4*self.val5)

    def div(self):
        if 0 in [self.val1,self.val2,self.val3,self.val4,self.val5]:
        # try:
            print('cannot divide by zero')
        else:
            print('Division: ',self.val1/self.val2/self.val3/self.val4/self.val5)
        # except ZeroDivisionError:
            # print('Cannot  divide by zero')
    
    def mod(self):
        if 0 in [self.val1,self.val2,self.val3,self.val4,self.val5]:
            print('it cant  allow  modulus by 0 ')
        else:
            print('Modulus: ',self.val1%self.val2%self.val3%self.val4%self.val5)
    
    def min(self):
        print ('Smallest number: ',min(self.val1,self.val2,self.val3,self.val4,self.val5))

    def max(self):
        print ('Largest number: ',max(self.val1,self.val2,self.val3,self.val4,self.val5))
    
    def mean(self):
        print('Mean: ', (self.val1+self.val2+self.val3+self.val4+self.val5)/5)
    
    def median(self):
        num = [self.val1,self.val2,self.val3,self.val4,self.val5]
        num.sort()
        print('Median: ', num[2])
    
    def total_75per(self):
        print('75% of total: ', (75*(self.val1+self.val2+self.val3+self.val4+self.val5))/100)
    
    def total_50per(self):
        print('50% of total: ', (50*(self.val1+self.val2+self.val3+self.val4+self.val5))/100)
    
    def total_25per(self):
        print('25% of total: ', (25*(self.val1+self.val2+self.val3+self.val4+self.val5))/100)


m1 = calci(97,61,29,17,2)
m1.add()
m1.sub()
m1.multi()
m1.div()
m1.mod()
m1.min()
m1.max()
m1.mean()
m1.median()
m1.total_75per()
m1.total_50per()
m1.total_25per()