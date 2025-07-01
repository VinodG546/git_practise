str1=input("enter str:")
result={}
 
prev=str1[0]
count=1
for i in range(1,len(str1)):
    if str1[i]==prev:
        count+=1
    else:
        result[prev]=count
        prev=str1[i]
        count=1
result[prev]=count
print(result)