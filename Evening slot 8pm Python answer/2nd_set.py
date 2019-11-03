n=int(input())
frnds = list(map(int,input().split()))
max=0
for i in frnds:
  for j in frnds:
    if(i%j>=max):
      max=i%j
print(max,end="")





/*  2nd method*/
n=int(input())
f=list(map(int,input().split(" ")))
a=[]
for i in range(n):
    for j in range(n):
        b=f[i]%f[j]
        a.append(b)
print(max(a),end="")
