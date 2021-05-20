# Jason Zhang
# jasozhang
# 112710259
# CSE 101
# Homework 6

import re


# Part I
def find_special_tokens(words):
    pattern = r'^[a-z]{2}\d{1,3}$'
    y = []
    for i in range(len(words)):
        x = re.match(pattern, words[i])
        if x:
            y.append(i)
    return y


# Part II
def find_suitable_names(names):
    suitable = []
    pattern = r'^[^aeiou].[A-Za-z][^aeiou]$'
    for i in names:
        x = re.match(pattern, i)
        if x:
            suitable.append(i)
    return suitable


# Part III
def math_expr(expressions):
    pattern = r'[+-]\d+\s+[-+*/^]\s+[+-]\d+$'
    non = []
    for i in expressions:
        x = re.match(pattern, i)
        if x:
            non.append(expressions.index(i))
    return non


# Part IV
def remove_italics(sentence):
    pattern = r'<i>(.*?)</i>'
    return re.sub(pattern, r'\1 \1', sentence)


# Part V
def scramble(plaintext, salt, step):
    x = ''
    y = 0
    for i in plaintext:

        if y + step > len(salt):
            yu = (y + step) - len(salt)
            x += salt[y: (len(salt))]
            y = 0
            x += salt[y: y + yu]
            y += yu
            if y == len(salt):
                y = 0

        else:
            x += salt[y: y + step]
            y += step
        x += i
    return x


# Part VI
def unscramble(encrypted, step):
    x = ''
    for i in range(step, len(encrypted), step + 1):
        x += encrypted[i]
    return x


# Part VII
def cafe_day(orders):
    sum = 0
    if len(orders) == 0:
        return float(0.0)
    else:
        for i in orders:
            if len(i) == 4 and (i[0] == 'P' or i[0] == 'G' or i[0] == 'S') and i[1] >= 0 and i[2] >= 0 and i[3] >= 0:
                print(sum)

                if i[0] == 'P':
                    if i[1] >= 3 or i[2] >= 4:
                        if i[3] >= 3:
                            i[3] -= 3
                        else:
                            i[3] = 0
                    sum += (i[1] * 3.5) + (i[2] * 2.5) + (i[3] * 1.25)
                elif i[0] == 'G':
                    if i[1]+i[2]+i[3] >= 10:
                        sum += ((i[1] * 3.5) + (i[2] * 2.5) + (i[3] * 1.25))-((i[1] * 3.5) + (i[2] * 2.5) + (i[3] * 1.25))*0.2
                    else:
                        sum += ((i[1] * 3.5) + (i[2] * 2.5) + (i[3] * 1.25))
                elif i[0] == 'S':
                    sum += ((i[1] * 3.5) + (i[2] * 2.5) + (i[3] * 1.25))-((i[1]*3.5)+(i[2]*2.5)+(i[3]*1.25))*0.02
        return sum



# Part VIII
def blackjack_dice(dice):
    player1 = 0
    player2 = 0
    condition = False
    p1rolldice = True
    p2rolldice = True
    i = 0
    winner = []
    while condition == False:
        if p1rolldice:
            print('player1 turn', player1)
            if player1 < 16:
                player1 += dice[i] + dice[i + 1]
                i += 2
            if player1 == 21:
                condition = True
                p2rolldice = False
                winner = [1, player1]
            elif player1 > 21:
                condition = True
                p2rolldice = False
                winner = [2, player2]
            elif player1 >= 16:
                p1rolldice = False
        if p2rolldice:
            print('player2 Turn', player2)
            if player2 < 16:
                player2 += dice[i] + dice[i + 1]
                i += 2
            if player2 == 21:
                condition = True
                p1rolldice = False
                winner = [2, player2]
            elif player2 > 21:
                condition = True
                p1rolldice = False
                winner = [1, player1]
            elif player2 >= 16:
                p2rolldice = False
        if p2rolldice == False and p1rolldice == False:
            condition = True
            if player2 > player1:
                winner = [2, player2]
            elif player1 > player2:
                winner = [1, player1]
            else:
                winner = [0, 0]
    return winner
