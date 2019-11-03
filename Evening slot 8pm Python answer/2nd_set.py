n=int(input())
frnds = list(map(int,input().split()))
max=0
for i in frnds:
  for j in frnds:
    if(i%j>=max):
      max=i%j
print(max,end="")