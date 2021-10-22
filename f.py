f=open("f.txt","r")
v=f.readlines()
i=0
c=0
while i<len(v):
    if "\n" in v[i]:
        c=c+1
    i=i+1
print(c,'number of lines present.')
print(v,"lines")

f.close()
# counting the n umber of lines
