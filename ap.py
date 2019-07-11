ru,ki=input().split()
jk13=abs(len(ki)-len(ru))
for g in range(len(ru)):
    if(len(ki)==1 and ki[g] in ru):
        break
    if (ru[g]!=ki[g]):
        jk13=jk13+1
print(jk13)
