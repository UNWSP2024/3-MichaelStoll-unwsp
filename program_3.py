#title: shipping charges
#author: michael stoll
#date: 2/5/25
lb=float(input('Total weight:'))
if lb<=2:
    print('Shipping fee:','$1.50')
elif 2<lb<=6:
    print('Shipping fee:','$3.00')
elif 6<lb<=10:
    print('Shipping fee:','$4.00')
else:
    print('Shipping fee:','$4.75')