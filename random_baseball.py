import random

list_a=[]
st_count=0
bl_count=0

while len(list_a)<3:
    n=random.randint(1,9)
    if n not in list_a:
        list_a.append(n)




while st_count!=3:
    y=input('3자리 정수를 입력하시요')
    list_b=[int(y[0]),int(y[1]),int(y[2])]
    
    for a,nm1  in enumerate(list_a):
        for b,nm2  in enumerate(list_b):
            if nm1==nm2:
                if a==b:
                    st_count+=1
                else:
                    bl_count+=1
    print("strike {}, ball {}". format(st_count, bl_count))
    st_count=0
    bl_count=0

