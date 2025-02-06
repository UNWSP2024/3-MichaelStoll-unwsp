#title: age classifier
#author: michael stoll
#date: 2/5/25
a=int(input('Enter age here:'))
if a<=1:
    print('You are an infant')
elif 1<a<13:
    print('You are a child')
elif 13<=a<20:
    print('You are a teenager')
else:
    print('You are an adult')