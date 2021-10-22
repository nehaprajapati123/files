dic={
    "bat":"bat",
    'bat':4,
    "wicket":8,
    "ball":"green",
    "bat":3
    }
dic1={}
for i in dic:
    if dic[i] not in dic1:
        dic1.update(dic[i])
    print(dic1)
    

