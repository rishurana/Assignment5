if(year%400==0)or(year%4==0)and(year%100!=0):
  print("year is leap")
else
  print("year is not leap yaer")


l=int(input("enter any length"))
b=int(input("enter any breadth"))
if(l==t):
 print("dimension are of square")
else:
 print("dimension are of rectangle")



x=int(input("enter your age"))
y=int(input("enter your age"))
z=int(input("enter your age"))
if(x>y):
 print("x is older")
else:
 print("z is older")
else:
 if(y>x):
 print("y is older")
 else:
 print("z is older")


a=int(input("enter the points:"))
f=1
if a<200:
 if 1<a<50:
   f=0
   print("No Prize")
 elif 50<a<150:
      prize="Wooden Box"
 elif150<a<180:
      prize="Book"
 elif180<a<200:
      prize="Chocolate"
 if f!=0:
      print("Congratulations you won a {}".format(prize))



n=int(input("enter the cost:"))
p=n*100
if p>1000:
   disc=P*.1
   r=p-disc
   print('total.cost= ',r)
