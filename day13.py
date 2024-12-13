import re # Don't upload that to the web page, it isn't necesary

def is_robot_back(moves: str) -> bool | list[int]:
    moves_values = {'L': [-1, 0], 'D': [0, -1], 'R': [1, 0], 'U': [0, 1]}
    init_pos = [0, 0]
    moves_done = set()
    moves = re.sub(r"\*(.)", lambda m: m.group(1) * 2, moves)
    moves = re.sub(r"\!R", "L", moves)
    moves = re.sub(r"\!L", "R", moves)
    moves = re.sub(r"\!U", "D", moves)
    moves = re.sub(r"\!D", "U", moves)
    moves_iter = iter(moves)
        
    for move in moves_iter:
        if move == '?':
            next_move = next(moves_iter, None)

            if next_move and next_move not in moves_done:
                move = next_move

        if move in moves_values:
            init_pos[0] += moves_values[move][0]
            init_pos[1] += moves_values[move][1]

        moves_done.add(move)

    return True if init_pos[0] == 0 and init_pos[1] == 0 else init_pos


# Tests by hand:
# if __name__ == "__main__":
#     moves = input("Movimientos: ")
#     print(is_robot_back(moves))
