# f=open("write.txt","w")
# name=input('enter your name\n')
# value=f.write(name)
# print(value)
# f.close



# f=open("write.txt","w")
# name=input('enter your name\n')
# f.write(name)
# f.close

f=open("write.txt","w")
i=0
while i<=5:
    name=input('enter your name\n')
    f.write(name)
    f.write('\n')
    i=i+1
f.close()
