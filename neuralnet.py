import random 

def neuralnet(state, player): 
    j = 0
    player2 = player.copy()
    for i in range(len(state)): 
        player2[j] = int(state[i]) * player2[j]
        player2[j + 1] = int(state[i]) * player2[j + 1]
        player2[j + 2] = int(state[i]) * player2[j + 2]
        j += 3
    
    up = player2[0] + player2[3] + player2[6] + player2[9] + player2[12] + player2[15]
    left = player2[1] + player2[4] + player2[7] + player2[10] + player2[13] + player2[16]
    right = player2[2] + player2[5] + player2[8] + player2[11] + player2[14] + player2[17]

    options = ['F', 'L', 'R']
    if up == left == right: 
        return random.choice(options)
    elif up == left: 
        return random.choice(options[0:2])
    elif left == right: 
        return random.choice(options[1:])
    elif up ==right: 
        return random.choice([options[0], options[2]])
    elif up > right: 
        if up > left: 
            return options[0]
        else: 
            return options[1]
    elif right > left: 
        return options[2]
    else: 
        return options[1]


