import turtle as t   # as 옵션은 단축 명령어 지정

t.shape("turtle")  # 커서가 거북이가됨
t.width(3)  # 펜 두께
t.shapesize(3,3)

while True :     # 무한 게임 실행
    command = input("명령 입력: ")

    if command == 'l' :
        t.left(90)
        t.forward(100)
    if command == 'r' :
        t.right(90)
        t.forward(100)
    if command == 'q' :
        break

