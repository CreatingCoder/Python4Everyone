import random

choices = ['Rock', 'Paper', 'Sissors']
randElement = choices[random.randint(0,2)]

try:
    userInput = input("Enter 0 for rock, 1 for paper, or 2 for sissors and press enter: ").lower()

except:
    print('Error: you did not input a 0, 1, or 2')

print('Rock, Paper, Sissors, Shoot!')

print('I got ' + randElement + ' and you got ' + choices[int(userInput)])


if(randElement == choices[int(userInput)]):
    print('It\'s a stalemate')

elif(randElement == 'Sissors' and choices[int(userInput)]== 'Paper'):
    print('I won!')

elif(randElement == 'Sissors' and choices[int(userInput)]== 'Rock'):
    print('You won!')

elif(randElement == 'Paper' and choices[int(userInput)]== 'Rock'):
    print('I won!')

elif(randElement == 'Paper' and choices[int(userInput)]== 'Sissors'):
    print('You won!')

elif(randElement == 'Rock' and choices[int(userInput)]== 'Paper'):
    print('You won!')

elif(randElement == 'Rock' and choices[int(userInput)]== 'Sissors'):
    print('I won!')

