ka,ma=map(str,input().split())
wasan13=0
if len(ka)>len(ma):
  ka,ma=ma,dbaj13
i=0
while i<len(ka):
  wasan13+=(ord(ma[i])-ord(k[i]))
  i+=1
for i in range(i,len(ma)):
  wasan13+=ord(ma[i])-ord('a')+1
print(wasan13)
