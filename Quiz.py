scores = []
name = input('What is your name? ')
print(f'Hello {name}, i would like you to answer the following questions.')
print('Read questions carefully and write the correct option')
starting = input('Enter start to start the quiz or quit to quit: ').lower()
if starting == 'start':
    print('Okay, we are ready to start')
    No_1 = (input('1. Opposite of Good? (A) Bad (B) Happy (C) Read (D) Come ')).upper()
    if No_1 == 'A':
        print('Correct')
        scores.append(No_1)
    else:
        print('Wrong')
    No_2 = (input('2. My Favorite Sport? (A) Basketball (B) Football (C) Hockey (D) Tennis ')).upper()
    if No_2 == 'B':
        print('Correct')
        scores.append(No_2)
    else:
        print('Wrong')
    No_3 = (input('2. My Favorite Musician? (A) Davido (B) Burna boy (C) Wizkid (D) Asake ')).upper()
    if No_3 == 'C':
        print('Correct')
        scores.append(No_3)
    else:
        print('Wrong')
    No_4 = (input('2. My Favorite Season? (A) Spring (B) Summer (C) Autumn (D) Winter ')).upper()
    if No_4 == 'B':
        print('Correct')
        scores.append(No_4)
    else:
        print('Wrong')
    No_5 = (input('2. My Favorite Club? (A) Arsenal (B) Chelsea (C) Barcelona (D) PSG ')).upper()
    if No_5 == 'A':
        print('Correct')
        scores.append(No_5)
    else:
        print('Wrong')
    Total_score = len(scores)
    print(f'Your Total score is {Total_score}')
elif starting == 'quit':
    print('Goodbye')
else:
    print('Error')

    




