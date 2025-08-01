import math

def getRootCooltime(grow, cool):
    weight = 1.0
    pow = 2
    while 100 < grow:
        p = math.pow(2, pow)
        weight *= (p - 1) / p
        grow -= 100
        pow += 1
    p = math.pow(2, pow)
    weight *= math.pow((p - 1) / p, grow / 100)
    return cool / weight 

if __name__ == '__main__':
    length = 0
    grow, cool = [], []
    avg = 0
    print('입력 길이를 입력하시오.')
    length = int(input())
    print('육성치와 쿨타임을 입력하시오.')
    for i in range(length):
        g, c =  map(float, input().split())
        if g < 0 or c < 0:
            break
        grow.append(g)
        cool.append(c + 0.5)
    for i in range(length):
        avg += getRootCooltime(grow[i], cool[i])
    avg /= length
    print('초기 쿨타임 : ', avg)
