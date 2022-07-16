import random

def computer_guess():
    user = input("Digite 'pedra', 'papel' ou 'tesoura'. ")
    computer = random.choice(['pedra', 'papel', 'tesoura'])

    if user == computer:
        return 'It\'s a Tie!'

    if is_win(user, computer):
        return 'You won!'

    return 'You lost!'

def is_win(player, opponent):
    if (player == 'tesoura' and opponent == 'papel') \
        or (player == 'papel' and opponent == 'pedra') \
            or (player == 'pedra' and opponent == 'tesoura'):
        return True
    
print(computer_guess())