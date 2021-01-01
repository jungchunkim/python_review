print ("베스킨로빈스 31 게임 시작")

number=1

while number < 31:
    while True:
        play1=int(input("(0은종료) 플레이어 1번 순서, 숫자입력: "))
        if play1 ==0:
            break
        if play1 < number or play1 > number:
            print('잘못입력했습니다. 다시 입력:')
            continue
        number= play1+1
    for i in range(number,32):
        print(i, end= ' ')

        
    
    
