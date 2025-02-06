n=int(input("enter a 4 digit number"))
odd=0
even=0
a=int(n/1000)
if a%2==0:
    even=even+a
else:
    odd=odd+a
n=n-(a*1000)
a=int(n/100)
if a%2==0:
    even=even+a
else:
    odd=odd+a
n=n-(a*100)
a=int(n/10)
if a%2==0:
    even=even+a
else:
    odd=odd+a
print("sum of even digits: ",even)
print("sum of odd digits: ",odd)