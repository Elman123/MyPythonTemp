yourpoint = 0

question = input('Rusiyanin paytaxti?')
answer = 'Moskva'

if question == answer:
    print('Dogru')
    yourpoint+=1
    print(yourpoint, "Point")
else:
    print('Sehv')
    yourpoint-=1
    print(yourpoint, "Point")
    

question = input('Berlin haradadir?')
answer = 'Almanya'

if question == answer:
    print('Dogru')
    yourpoint+=1
    print(yourpoint, "Point")
else:
    print('Sehv')
    yourpoint-=1
    print(yourpoint, "Point")
    

question = input('En boyuk okean?')
answer = 'Sakit'

if question == answer:
    print('Dogru')
    yourpoint+=1
    print(yourpoint, "Point")
else:
    print('Sehv')
    yourpoint-=1
    print(yourpoint, "Point")
    
    

question = int(input("Elmanin ad gunu necenci ay :)"))
answer = '6'

if question == answer:
    print('Dogru')
    yourpoint+=1
    print(yourpoint, "Point")
else:
    print('Sehv')
    yourpoint-=1
    print(yourpoint, "Point")
    
    
question = int(input("Elmanin ad gunu necenci il :)"))
answer = '2008'

if question == answer:
    print('Dogru')
    yourpoint+=1
    print(yourpoint, "Point")
else:
    print('Sehv')
    yourpoint-=1
    print(yourpoint, "Point")