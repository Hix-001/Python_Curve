#WAP to check if a number entered by user is even or odd
x=int(input("Enter a number:"))
if(x%2==0):
   print (x,"Is an even number")
else :
   print (x,"Is an odd number")

#WAP to find the greatest of 3 numbers entered by user
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))    
c=int(input("Enter third number:"))
if (a>b and a>c):
	print (a,"is the greatest number out of",a,",",b,"&",c)
if (b>a and b>c):
	print (b,"is the greatest number out of",a,",",b,"&",c)
if (c>a and c>b):
	print (c,"is the greatest number out of",a,",",b,"&",c)
#OR 
if (a>=b and a>=c):
    print (a,"is the greatest number out of",a,",",b,"&",c)
elif (b>=c):
    print (b,"is the greatest number out of",a,",",b,"&",c)
else:   
    print (c,"is the greatest number out of",a,",",b,"&",c)

#WAP to check if a number entered by user is a multiple of 7 or not 
x=int(input("Enter a number: "))
if(x%7==0):
	print(x,"is a multiple of 7")
else : 
	print(x,"is not a multiple of 7")
      