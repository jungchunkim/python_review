# 동전던지기 + 터틀

import random
import turtle
#t.shape("turtle")

# 이미지파일은 소스랑 같은 경로에 위치시킨다.
# 경로가 다른 경우에는 경로명까지 기입한다
screen = turtle.Screen()
image1 = 'f1.png'   # 확장자는 추후에 변경할 수 있다
image2 = 'b1.png'
screen.addshape(image1)
screen.addshape(image2)

t = turtle.Turtle()
coin = random.randint(0, 1)

if coin == 0 :
    t.shape(image1)
    t.stamp()
else :
    t.shape(image2)
    t.stamp()
