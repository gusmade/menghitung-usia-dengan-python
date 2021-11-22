#import module
import numpy as np

today = dt.date.today()
# aks user to input data
tgl = int (input(" input your date = "))
bln = int (input ("input your moon = " ))
thn =  int (input (" input your year = "))

birtday = dt.date(thn,bln,tgl)
print (birtday, f" day= {birtday : %a}")
age = today - birtday 
age_year = age.days //365
print ("your age = " , age_year)
