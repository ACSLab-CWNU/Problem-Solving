import sys
def stone_move(move,stone_index):
    tnp_stone = list(stone_index)
    if move == 'R':
        tnp_stone[0] += 1
    elif move == 'L':
        tnp_stone[0] -= 1
    elif move == 'B':
        tnp_stone[1] -= 1
    elif move == 'T':
        tnp_stone[1] += 1
    elif move == 'RT':
        tnp_stone[0] += 1
        tnp_stone[1] += 1
    elif move == 'LT':
        tnp_stone[0] -= 1
        tnp_stone[1] += 1
    elif move == 'RB':
        tnp_stone[0] += 1
        tnp_stone[1] -= 1
    elif move == 'LB':
        tnp_stone[0] -= 1
        tnp_stone[1] -= 1

    return tnp_stone

def king_stone_move(move,king_index,stone_index):
    tmp_king = list(king_index)
    tmp_stone = list(stone_index)
    if move == 'R':
        tmp_king[0] += 1
    elif move == 'L':
        tmp_king[0] -= 1
    elif move == 'B':
        tmp_king[1] -= 1
    elif move == 'T':
        tmp_king[1] += 1
    elif move == 'RT':
        tmp_king[0] += 1
        tmp_king[1] += 1
    elif move == 'LT':
        tmp_king[0] -= 1
        tmp_king[1] += 1
    elif move == 'RB':
        tmp_king[0] += 1
        tmp_king[1] -= 1
    elif move == 'LB':
        tmp_king[0] -= 1
        tmp_king[1] -= 1

    if tmp_king[0] < 0 or tmp_king[1] < 0 or tmp_king[0] > 7 or tmp_king[1] > 7 :
        return king_index, stone_index
    else:
        if tmp_king == tmp_stone:
            tmp_stone = stone_move(move, tmp_stone)

            if tmp_stone[0] < 0 or tmp_stone[1] < 0 or tmp_stone[0] > 7 or tmp_stone[1] > 7 :
                return king_index, stone_index
            else:
                return tmp_king, tmp_stone
            return tmp_king, tmp_stone
        else:
            return tmp_king, tmp_stone
        return tmp_king, tmp_stone

def position_index(matrix,king,stone):
    position_king = []
    position_stone = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if(matrix[i][j] == king):
                position_king.append(i)
                position_king.append(j)
            elif(matrix[i][j] == stone):
                position_stone.append(i)
                position_stone.append(j)
    return position_king, position_stone

# Main function start
row = ['A','B','C','D','E','F','G','H']
matrix = [[row[j]+str(col) for col in range(1,9)] for j in range(8)]
king, stone, N = list(map(str, input().split()))
king_index, stone_index = position_index(matrix,king,stone)
king_result, stone_result = list(king_index), list(stone_index)
movelist = []
for i in range(int(N)):
    move = input()
    movelist.append(move)
#런타임에러가 나서 입력받을때마다 처리해주면 안되 
for moving in movelist:
    king_result, stone_result = king_stone_move(moving,king_result,stone_result)
    
print(matrix[king_result[0]][king_result[1]])
print(matrix[stone_result[0]][stone_result[1]])