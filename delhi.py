def file(state):
        if state=="delhi":
                f=open("delhi.txt","r")
                w=f.read()
                print(w)
                f.close()
state=input('enter state\n')
file(state)