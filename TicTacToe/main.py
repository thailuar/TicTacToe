table = [' ' for _ in range(9)]


def print_table():
    print('-------------')
    print('| ' + table[0] + ' | ' + table[1] + ' | ' + table[2] + ' |')
    print('-------------')
    print('| ' + table[3] + ' | ' + table[4] + ' | ' + table[5] + ' |')
    print('-------------')
    print('| ' + table[6] + ' | ' + table[7] + ' | ' + table[8] + ' |')
    print('-------------')


def check_win(player):
    for i in range(0, 9, 3):
        if table[i] == table[i+1] == table[i+2] == player:
            return True
    for i in range(3):
        if table[i] == table[i+3] == table[i+6] == player:
            return True
    if table[0] == table[4] == table[8] == player or table[2] == table[4] == table[6] == player:
        return True
    return False


def play_game():
    print('Bem vindo ao jogo da velha!')
    print_table()
    player = 'X'
    while True:
        move = input('Player ' + player + ', escolha um número (1-9): ')
        try:
            move = int(move) - 1
            if table[move] != ' ':
                print('Este lugar já está preenchido :( Tente novamente.')
                continue
            table[move] = player
            print_table()
            if check_win(player):
                print('Player ' + player + ' é o vencedor!')
                break
            if ' ' not in table:
                print('Temos um empate!')
                break
            player = 'O' if player == 'X' else 'X'
        except ValueError:
            print('Oops, local inválido, escolha novamente ;)')


# Start the game
play_game()
