# tryexpect.py

strValue = 'Hello Bob'
try:
    intValue = int(strValue)
except:
    intValue = -1

print ('First ', intValue)

strValue = '123'
try:
    intValue = int(strValue)
except:
    intValue = -1

print ('Second ', intValue)


