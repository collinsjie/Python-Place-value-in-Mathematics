# Place value in Mathematics project
while True:
    number = int(input('Enter a number:'))
    if number >10000000000:
        break
    if 1<=number<=9:
        print('unit')
    elif 10<=number<=99:
        print('tens')
    elif 100<=number<=999:
        print('hundredes')
    elif 1000<=number<=9999:
        print('thousands')
    elif 10000<=number<=99999:
        print('Tens of thousands')
    elif 100000<=number<=999999:
        print('Hundreds of thousands')
    elif 1000000<=number<=9999999:
        print('Millions')
    elif 10000000<=number<=99999999:
        print('Tens of Millions')
    elif 100000000<=number<=999999999:
        print('Hundreds of Millions')
    elif number==1000000000:
        print('Billions')
    else:
        print('break')
