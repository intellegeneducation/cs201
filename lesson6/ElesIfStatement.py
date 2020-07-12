#ElseIfStatement
score = eval(input("Enter your score (0 ~ 100):"))
# A : >= 90
# B : >= 80
# C : >= 70
# D : >= 60
# F : all other

if score >= 90:     # boolean: true or false
    print ("you get a A")
elif score >= 80:   # boolean: true or false
    print ("you get a B")
elif score >= 70:   # boolean: true or false
    print ("you get a C")
elif score >= 60:   # boolean: true or false
    print ("you get a D")
else: # alway true
    print ("you get a F")
