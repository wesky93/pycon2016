from random import choice

def 반대손모양(손모양):
    """반대다 손모양을 알려준"""
    if 손모양 == 'gawi':
        return 'bawi'
    elif 손모양 == 'bawi':
        return 'bo'
    else:
        return 'gawi'

def show_me_the_hand(records):
    # 100번 까지는 무작위
    try:
        if len(records) <= 100:
            return 'gawi'
        elif len(records) <= 200:
            return 'bawi'
        else:
            return 'bo'
    except:
        return choice(['gawi', 'bawi', 'bo'])
