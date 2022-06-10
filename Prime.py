b=[]
for i in range (1,44):
  count=0
  for j in range(2,i):
    if (i % j) == 0:
      count=count+1
  if count==0:
    b.append(i)
c=tuple(b)
z=list(b)
k=0
for i in range(0,5):
  for j in range(0,i+1):
    print(z[k],end=" ")
    k=k+1
  print("\n")


