arr =[1,2,3]
value = 0
for x in arr:
    value = (value + x)*10
    #print(value)
    v = value // 10
print(v)
rev = 0
while(v > 0):
    rev = (rev*10) + v %10
    v = v//10
    print(rev)


 


    


    

   

