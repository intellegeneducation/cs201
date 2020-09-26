hours = float(input('Enter Hours:'))
rate = float(input('Enter Rate:'))

payment = 0
if hours <= 40:
    payment = hours * rate
if hours > 40:
    payment = (40 * rate) + ((hours - 40) * (rate * 1.5))
    
print(payment)
