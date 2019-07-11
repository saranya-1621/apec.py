vsa12,vita112=map(str,input().split())
wasa12=0
if len(vsa12)>len(vita112):
  vsa12,vita112=vita112,dbja12
i=0
while i<len(vsa12):
  wasa12+=(ord(vita112[i])-ord(vsa12[i]))
  i+=1
for i in range(i,len(vita112)):
  wasa12+=ord(vita112[i])-ord('a')+1
print(wasa12)
