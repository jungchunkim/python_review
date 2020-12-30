import random
time = random.randint(1, 24)
sunny = random.choice([True, False])

print("좋은 아침입니다. 지금 시각은",  str(time)+"시 입니다")

#while True :
# 날씨여부 판단
if sunny :
    print("날씨가 화창합니다")
else :
    print("날씨가 화창하지 않습니다")

# 새의 노래 여부 판단
if time >= 6 and time <= 9 and sunny :
    print("새가 노래를 한다")
else :
    print("새가 노래하지 않는다")
