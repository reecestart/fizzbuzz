tracker = 0
while tracker < 100:
    tracker = tracker + 1
    dividebythree = tracker / 3
    if dividebythree.is_integer():
        dividebyfive = tracker / 5
        if dividebyfive.is_integer():
            print('fizzbuzz')
        else:
            print('fizz')
    else:
        dividebyfive = tracker / 5
        if dividebyfive.is_integer():
            print('buzz')
        else:
            print(tracker)