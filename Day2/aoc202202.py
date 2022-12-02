def main():
    with open(r'D:\Users\Pantai Suyasri\Documents\Programming\advent-of-code-2022\Day2\input.txt', 'r') as f:
        lines = f.read()

    games = lines.split('\n')
    games = [game.split(' ') for game in games]

    lookup = {
        0: {0: 3, 1: 6, 2: 0},
        1: {0: 0, 1: 3, 2: 6},
        2: {0: 6, 1: 0, 2: 3},
    }

    totalScore = 0
    # part 1
    for game in games:
        a = ord(game[0]) - ord('A')
        b = ord(game[1]) - ord('X')

        totalScore += (b + 1)
        totalScore += lookup[a][b]
    print(totalScore)

    totalScore = 0
    # part 2
    for game in games:
        a = ord(game[0]) - ord('A')
        command = ord(game[1]) - ord('X')

        if command == 0:
            b = list(lookup[a].keys())[list(lookup[a].values()).index(0)]
        elif command == 1: 
            b = list(lookup[a].keys())[list(lookup[a].values()).index(3)]
        elif command == 2: 
            b = list(lookup[a].keys())[list(lookup[a].values()).index(6)]
        
        totalScore += (b + 1)
        totalScore += lookup[a][b]
    print(totalScore)


if __name__ == '__main__':
    main()
