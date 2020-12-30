age = input("생후 몇개월: ")
age = int(age)

if 0 <= age <= 1 :
    print("결핵 접종")
if 0 <= age <= 2 :
    print("B형 간염 접종")
if 2 <= age <= 6 :
    print("파상풍 접종")
if 2 <= age <= 15 :
    print("폐렴구균접종")
    
