from turtle import *
#色
color('blue', 'yellow')
#color塗りつぶし
begin_fill()
#fill同じ値の配列リストを作る
while True:
    forward(200)
#頭を向けている方向へ
    left(175)
#170だけ左に向ける
    if abs(pos()) < 1:
        break
#pos(）は「タートルの現在位置をVec2D a の絶対値」を返します。
#abs(a)は[Vec2D  a　]
end_fill()
done()
