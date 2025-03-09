def read_file(filename):
    with open(f'illustrations/{filename}', 'r') as file:
        content = file.read()
    return content

def scissors():
    return read_file('scissors.txt')

def rock():
    return read_file('rock.txt')

def paper():
    return read_file('paper.txt')

def loser():
    return read_file('loser.txt')

def winner():
    return read_file('winner.txt')

def tie():
    return read_file('tie.txt')