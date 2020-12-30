import turtle as t
# as 옵션은 단축 명령어 지정이다.

t.shape("turtle")  # 커서가 거북이가됨

t.penup()  # 거북이 이동시 그림 그리지 않는다.

# t.goto(x좌표, y좌표)
t.goto(100, 100)
t.write("거북이가 여기로 오면 양수입니다")

t.goto(100, 0)
t.write("거북이가 여기로 오면 0입니다")

t.goto(100, -100)
t.write("거북이가 여기로 오면 음수입니다")
