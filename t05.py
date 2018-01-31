# passport = []# [] -- list; ()- cortege
passport = input("type your name  and (after 'space' symbol) surname\n").split(' ')
if len(passport)==2:
    print(passport[1]+' '+passport[0])
else:
    print("error 239: incorrect input")