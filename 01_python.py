import os
#Load Module
import modulefinder
import math


print("Hello Sudip Acharya")

#This is the single line comment
'''This is the 
Multiple Lline Comments'''

#List Module finder contents
dir(modulefinder)
#Call function from module finder
modulefinder.funcl()

#check data type
type(variable)

#Special Character in string can be done via \ or preface with r
strl = r'this\f?ff'
#String formatting can be done in a number of ways like
template = '%.2f %s hah $%d';
strl = template % (4.88, 'hola', 2)

#None is a common default value for optional function arguments
def funcl(a,b,c = None):
    #common usages of None
    variable = a
    if variable is None:
        print(f'{b}')

# 'datetime' combines information stored in 'date' and 'time'
import datetime

#create datetime from string
dtl = datetime.strptime('20230414', '%Y%m%d')
#Get 'date' object
dtl.date()
#Get 'time' object
dtl.time()
#Format datetime to string
dtl.strftime(' %m/%d/%Y %H:%M')
#Change Field Value
dt2 = dtl.replace(minute=0, second = 30)
#Get Differnce
dt1 = dt.date()
diff = dt1 -dt2
#duff us a 'datetime.timedelta' object