import player as player1
import ramdomplay as player2

class 결과:
    def __init__(self):
        self.계수 = 0
        self.승 = 0
        self.패 = 0
        self.비김 = 0

    계수 = 0
    def add(self,상태):
        self.계수 += 1
        if 상태 == 1:
            self.승 += 1
        elif 상태 == -1:
            self.패 += 1
        else:
            self.비김 += 1

    def result(self):
        승률 = self.승/1000*100
        return (self.계수, 승률)



def countpoint(r):
    가위 = 결과()
    바위 = 결과()
    보 = 결과()
    승합 = 0
    비김합 = 0
    짐합 = 0

    for i in r:
        # 이겼을 경우
        if i[1] == 0:
            짐합 += 1
        # 비긴 경
        elif i[1] == 1:
            승합 += 1
        else:
            비김합 += 1

        # 가위바위보 계수
        if i[0] == 'gawi':
            가위.add(i[1])
        # 비긴 경우
        elif i[0] == 'bawi':
            바위.add(i[1])
        else:
            보.add(i[1])

    return (승합,비김합,짐합,가위.result(),바위.result(),보.result())

r1 = []
r2 = []
for i in range(1000):
    h1 = player1.show_me_the_hand(r2)
    h2 = player2.show_me_the_hand(r1)
    if h1 == h2:
        print('match %d of 1000: tie' % i)
        r = 0
    elif (h1 == 'gawi' and h2 == 'bo') or (h1 == 'bawi' and h2 == 'gawi') or (h1 == 'bo' and h2 == 'bawi'):
        print('match %d of 1000: p1 win' % i)
        r = 1
    else:
        print('match %d of 1000: p2 win' % i)
        r = -1
    r1.append((h1, r))
    r2.append((h2, -r))
    # blah blah ...

win,tie,lose,가위,바위,보 = countpoint(r1)
print('player1 승:{0},비김:{1},패:{2}, //각 손모양별 승률 가위:{3},바위:{4},보:{5}'.format(win,tie,lose,가위,바위,보))

win,tie,lose,가위,바위,보 = countpoint(r2)
print('player1 승:{0},비김:{1},패:{2}, //각 손모양별 승률 가위:{3},바위:{4},보:{5}'.format(win,tie,lose,가위,바위,보))