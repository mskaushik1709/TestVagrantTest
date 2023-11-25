product=['Leather wallet', 'Umbrella', 'Cigarette', 'Honey']
price=[1100,900,200,100]
gst=[18,12,28,0]
quantity=[1,4,3,2]
q=[]
#unit price
for i in range(len(price)):
    q.append(price[i]/quantity[i])
    
    if q[i]>500:
            q[i]=q[i]-(q[i]*5/100)
u=[]
#gst
for j in range(len(q)):
      u.append(q[j]+(q[j]*gst[j]/100))
a=[]
#total
for i in range(len(u)):
      a.append(u[i]*quantity[i])
o=''
for i in range(len(u)):
      if (u[i]==max(u)):
            o=product[i]

print("The product of max Gst amount is",o)
print("Total amount paid is",sum(a))

