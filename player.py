from random import choice



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
