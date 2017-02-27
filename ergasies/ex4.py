x = int(input("How big do you want the list to be ?: "))
n = 0
new = x-4 
l1 = [ ] 
while x < 6: 
    print("Gia na doulepsei swsta to programma vale 6 oi perissoterous arithmous ")
    x = int(input("How big do you want the list to be ?: "))
while n < x : 
  n=n+1
  y = float(input("Dwse enan arithmo: "))
  l1.append (y) 
  print("H lista mas mexri stigmhs einai") ,  l1
l1.sort() 
print("H lista exei taksinomithei epitixws ") ,  l1
l1.pop() 
l1.pop() 
l1.reverse()
l1.pop()
l1.pop()
l1.reverse()
print("H lista mas mexri stigmhs einai ") ,  l1
k=0
sum=0
while k < new :
 sum = l1[k] + sum 
 k=k+1 
avg = sum/new 
print ("H mesh timh einai ") , avg
k=0
sum1=0 
sum2=0
result=0
while k < new :
 b = l1[k] - avg
 k=k+1 
 b = b **2 
 print"to b einai ", b 
 sum1= b +sum1 
 sum2=sum1 
 print "to sum 1 einai ", sum1 
 sum2=sum2/new 
 print "to sum 2 einai " ,sum2 
 result =sum2 **0.5 
print "H typiki apoklisi einai " , result