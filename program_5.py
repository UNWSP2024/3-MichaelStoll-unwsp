#title: hot dog
#author: michael stoll
#date: 2/5/25
#This is intended to look similar to a menu at a restaurant
print('''Menu:
1. Hot dog $3.50
2. Chili dog $4.50
Toppings:
0. No topping
1. Cheese $0.50
2. Peppers $0.75
3. Grilled onions $1.00''')
#hd is hot dog and t is topping. p stands for price
hd=int(input("Enter number corresponding to hot dog of choice here:"))
t=int(input("Enter number corresponding to topping of choice here:"))
if hd==1:
    hdp=3.5
elif hd==2:
    hdp=4.5
else:
    hdp=-1
if t==0:
    tp=0
elif t==1:
    tp=0.5
elif t==2:
    tp=0.75
elif t==3:
    tp=1
else:
    tp=-1
sub = hdp + tp
if hdp==-1 or tp==-1:
    print( "\n" + 'This order is invalid')
else:
    print('Subtotal:',sub)
    print('Tax: 7%')
    total=f"{sub*1.07:0.2f}"
    print('Total:',total)