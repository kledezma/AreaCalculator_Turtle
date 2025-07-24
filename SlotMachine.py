import random

symbols =  ['🍒',' 🍇', '🍉', '7️⃣']
exit = 'Y'


def play():
    result = random.choices(symbols, k=3)
    print(result)
    print('===================')
    if result[0] == '7️⃣' and result[1] == '7️⃣' and result[2] == '7️⃣' :
        print('Jackpot')
    else:
        print('Thank u for playing')

def askcontinue():
    response = input('Do you want to continue? Y/N')

    if response == 'N':
       global exit
       exit = 'N'


while exit == 'Y':
    play()
    askcontinue()


