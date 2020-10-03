# trynum.py

strValue = input('Enter a number:')
try: 
    intValue = int(strValue)
except: 
    intValue = -1

if intValue > 0 :  
    print ('Nice work')
else:  
    print ('Not a number')

