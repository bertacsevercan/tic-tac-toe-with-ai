# write your code here
import random
from copy import deepcopy

g_resume = True  # global var to store a condition for the while loop in the game func.
g_x = "X"
g_o = "O"
g_empty = " "
g_board = []


def create_board(n, board):
    n_empty = " " * n
    for i in range(len(n_empty)):
        board.append(list(n_empty))
    return board


create_board(3, g_board)


def show_board():
    board_str = ""
    for row in g_board:
        board_str += "| " + " ".join(row) + " |\n"
    dash_len = (len(board_str) // len(g_board) - 1) * "-"
    print(f"""{dash_len}
{board_str}{dash_len}""")


g_coordinate_dict = {
    ("1", "1"): [2, 0],
    ("1", "2"): [1, 0],
    ("1", "3"): [0, 0],

    ("2", "1"): [2, 1],
    ("2", "2"): [1, 1],
    ("2", "3"): [0, 1],

    ("3", "1"): [2, 2],
    ("3", "2"): [1, 2],
    ("3", "3"): [0, 2]
}


def sign(
        count):  # count is to count the turns passing in the game so that first player would be X and the second 'd be O
    if count % 2 == 0:
        return g_x
    return g_o


class win_check:
    board_len = len(g_board)
    empty = " "

    def __init__(self, board):
        self.board = board

    def horizontal_vertical(self):
        hori_to_vert_flat = []
        hori_to_vert_board = []
        x = 0
        y = 1
        for i in range(win_check.board_len):
            for j in range(win_check.board_len):
                hori_to_vert_flat.append(self.board[j][i])

        for i in range(win_check.board_len):
            hori_to_vert_board.append(hori_to_vert_flat[win_check.board_len * x:win_check.board_len * y])
            x += 1
            y += 1

            if hori_to_vert_board[i].count(g_x) == win_check.board_len:  # vertical check
                return g_x
            elif hori_to_vert_board[i].count(g_o) == win_check.board_len:
                return g_o

            if self.board[i].count(g_x) == win_check.board_len:  # horizontal check
                return g_x
            elif self.board[i].count(g_o) == win_check.board_len:
                return g_o

    def cross(self):
        a = []
        a_ = []
        x = 0
        y = 2

        for i in range(win_check.board_len):
            if len(a) == 0:
                a.append(self.board[i][i])
            elif a[-1] != self.board[i][i]:
                a.clear()
                a.append(self.board[i][i])
            elif a[-1] == self.board[i][i] and self.board[i][i] != win_check.empty:
                a.append(self.board[i][i])
                if len(a) == win_check.board_len:
                    return (a[0])

            if len(a_) == 0:
                a_.append(self.board[y][x])
            elif a_[-1] != self.board[y][x]:
                a_.clear()
                a_.append(self.board[y][x])
            elif a_[-1] == self.board[y][x] and self.board[y][x] != win_check.empty:
                a_.append(self.board[y][x])
                if len(a_) == win_check.board_len:
                    return (a_[0])
            x += 1
            y -= 1

    def check_draw(self):
        arr = []
        for i in range(len(self.board)):
            if win_check.empty not in self.board[i]:
                arr.append(1)
        return len(arr)

    def main(self):
        global g_resume
        if win_check.horizontal_vertical(self):
            player = win_check.horizontal_vertical(self)
            print(f"{player} wins")
            g_resume = False
        elif win_check.cross(self):
            player = win_check.cross(self)
            print(f"{player} wins")
            g_resume = False
        elif win_check.check_draw(self) == len(self.board):
            print("Draw")
            g_resume = False

    def score(self):
        global g_resume
        if win_check.horizontal_vertical(self):
            player = win_check.horizontal_vertical(self)
            return player
        elif win_check.cross(self):
            player = win_check.cross(self)
            return player


win_ch = win_check(g_board)


def check_empty_spots(board):
    empty_rows = []
    empty_cols = []
    empty_spots = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == g_empty:
                empty_rows.append(row)
                empty_cols.append(col)
                empty_spots.append([row, col])
    return [empty_rows, empty_cols, empty_spots]


def computer_medium_mode(sign, opposite_sign):
    d_ = {0: [g_board[2][0], g_board[1][1], g_board[0][2]],

          1: [g_board[0][0], g_board[1][1], g_board[2][2]],
          2: []}
    di_ = {
        0: [g_board[0][0], g_board[1][0], g_board[2][0]],
        1: [g_board[0][1], g_board[1][1], g_board[2][1]],
        2: [g_board[0][2], g_board[1][2], g_board[2][2]]}

    d = {0: [[2, 0], [1, 1], [0, 2]],

         1: [[0, 0], [1, 1], [2, 2]],
         2: []}
    di = {
        0: [[0, 0], [1, 0], [2, 0]],
        1: [[0, 1], [1, 1], [2, 1]],
        2: [[0, 2], [1, 2], [2, 2]]}

    for i in range(3):
        if g_board[i].count(sign) == 2 and g_empty in g_board[i]:
            print('Making move level "medium"')
            g_board[i][g_board[i].index(g_empty)] = sign
            break
        elif g_board[-i - 1].count(sign) == 2 and g_empty in g_board[-i - 1]:
            print('Making move level "medium"')
            g_board[-i - 1][g_board[-i - 1].index(g_empty)] = sign
            break
        elif d_[i].count(sign) == 2 and g_empty in d_[i]:
            x, y = d[i][d_[i].index(g_empty)]
            print('Making move level "medium"')
            g_board[x][y] = sign
            break
        elif di_[i].count(sign) == 2 and g_empty in di_[i]:
            x, y = di[i][di_[i].index(g_empty)]
            print('Making move level "medium"')
            g_board[x][y] = sign
            break
        elif g_board[i].count(opposite_sign) == 2 and g_empty in g_board[i]:
            print('Making move level  "medium"')
            g_board[i][g_board[i].index(g_empty)] = sign
            break
        elif g_board[-i - 1].count(opposite_sign) == 2 and g_empty in g_board[-i - 1]:
            print('Making move level  "medium"')
            g_board[-i - 1][g_board[-i - 1].index(g_empty)] = sign
            break
        elif d_[i].count(opposite_sign) == 2 and g_empty in d_[i]:
            x, y = d[i][d_[i].index(g_empty)]
            print('Making move level  "medium"')
            g_board[x][y] = sign
            break
        elif di_[i].count(opposite_sign) == 2 and g_empty in di_[i]:
            x, y = di[i][di_[i].index(g_empty)]
            print('Making move level  "medium"')
            g_board[x][y] = sign
            break
        else:
            print("random move")
            random_row = random.randint(0, 2)
            random_column = random.randint(0, 2)
            if g_board[random_row][random_column] == g_empty:
                g_board[random_row][random_column] = sign
                break


def computer_easy_mode(stop_condition, sign):
    random_row = random.choice(check_empty_spots(g_board)[0])
    random_column = random.choice(check_empty_spots(g_board)[1])
    if not stop_condition:  # checkpoint to stop the recursion
        pass
    elif g_board[random_row][random_column] == g_empty:
        print('Making move level "easy"')
        g_board[random_row][random_column] = sign
        return g_board[random_row][random_column]
    else:
        computer_easy_mode(stop_condition, sign)


def minimax(new_board, current_player, winner, loser):
    avail_spots = check_empty_spots(new_board)
    new_win_ch = win_check(new_board)
    win_result = new_win_ch.score()
    if win_result == winner:
        return {"score": 10}
    elif len(avail_spots[2]) == 0:
        return {"score": 0}
    elif win_result == loser:
        return {"score": -10}
    moves = []
    for i in range(len(avail_spots[2])):
        rows = avail_spots[0][i]
        cols = avail_spots[1][i]
        move = {"index": avail_spots[2][i]}
        new_board[rows][cols] = current_player
        if current_player == winner:
            result = minimax(new_board, loser, winner, loser)
            move["score"] = result["score"]
        else:
            result = minimax(new_board, winner, winner, loser)
            move["score"] = result["score"]
        new_board[rows][cols] = move["index"]
        moves.append(move)
    best_move = None
    if current_player == winner:
        best_score = -10000
        for i in range(len(moves)):
            if moves[i]["score"] > best_score:
                best_score = moves[i]["score"]
                best_move = i
    else:
        best_score = 10000
        for i in range(len(moves)):
            if moves[i]["score"] < best_score:
                best_score = moves[i]["score"]
                best_move = i
    return moves[best_move]


def computer_hard_mode(winner, loser):
    print('Making move level "hard"')
    clone_board = deepcopy(g_board)
    best_spot = minimax(clone_board, winner, winner, loser)
    row = best_spot["index"][0]
    col = best_spot["index"][1]
    g_board[row][col] = winner


def reset_board():
    for i in range(len(g_board)):
        for j in range(len(g_board)):
            g_board[i][j] = g_empty


def game_w_comp(mode, sign1, sign2):
    while g_resume:
        x, y = input("Enter the coordinates: ").split()
        cor_x, cor_y = [0, 0]
        try:
            cor_x, cor_y = g_coordinate_dict[x, y]
        except KeyError:
            pass

        if x.isdigit() is False or y.isdigit() is False:
            print("You should enter numbers!")

        elif int(x) > 3 or int(x) < 1 or int(y) < 1 or int(y) > 3:
            print("Coordinates should be from 1 to 3!")

        elif g_board[cor_x][cor_y] == g_empty:
            g_board[cor_x][cor_y] = sign1

        show_board()

        if mode == "easy":
            computer_easy_mode(g_resume, sign2)

        elif mode == "medium":
            computer_medium_mode(sign2, sign1)

        elif mode == "hard":
            computer_hard_mode(sign2, sign1)
        win_ch.main()
        show_board()


def game_w_users():
    count = 0
    while g_resume:
        x, y = input("Enter the coordinates: ").split()
        cor_x, cor_y = [0, 0]
        try:
            cor_x, cor_y = g_coordinate_dict[x, y]
        except KeyError:
            pass

        if x.isdigit() is False or y.isdigit() is False:
            print("You should enter numbers!")

        elif int(x) > 3 or int(x) < 1 or int(y) < 1 or int(y) > 3:
            print("Coordinates should be from 1 to 3!")

        elif g_board[cor_x][cor_y] == g_empty:
            g_board[cor_x][cor_y] = sign(count)

        else:  # if the cell occupied
            print("This cell is occupied! Choose another one!")

        show_board()
        win_ch.main()
        count += 1


def easy_vs_medium(count, sign1, sign2):
    if count % 2 == 0:
        computer_easy_mode(g_resume, sign1)

    else:
        computer_medium_mode(sign2, sign1)


def easy_vs_hard(count, sign1, sign2):
    if count % 2 == 0:
        computer_easy_mode(g_resume, sign1)

    else:
        computer_hard_mode(sign2, sign1)


def medium_vs_hard(count, sign1, sign2):
    if count % 2 == 0:
        computer_medium_mode(sign2, sign1)

    else:
        computer_hard_mode(sign1, sign2)


def run():
    options = ["easy", "medium", "user", "hard"]
    global g_resume
    while True:
        cmd, turn_x, turn_o = [None, None, None]
        user_input = input("Input command: ").split()
        if len(user_input) == 1:
            cmd = user_input[0]
        if len(user_input) == 2:
            cmd = user_input[0]
            turn_x = user_input[1]
        if len(user_input) == 3:
            cmd = user_input[0]
            turn_x = user_input[1]
            turn_o = user_input[2]

        if cmd == "start" and turn_x in options and turn_o in options:
            show_board()
            count = 0
            while g_resume:
                if turn_x == turn_o == "easy":
                    computer_easy_mode(g_resume, sign(count))
                elif turn_x == turn_o == "medium":
                    computer_medium_mode(sign(count), sign(count))
                elif turn_x == turn_o == "hard":
                    computer_hard_mode(sign(count), sign(count + 1))
                elif turn_x == turn_o == "user":
                    game_w_users()
                elif (turn_x, turn_o) == ("medium", "easy"):
                    easy_vs_medium(count, g_o, g_x)
                elif (turn_x, turn_o) == ("easy", "medium"):
                    easy_vs_medium(count, g_x, g_o)
                elif (turn_x, turn_o) == ("hard", "easy"):
                    easy_vs_hard(count, g_o, g_x)
                elif (turn_x, turn_o) == ("easy", "hard"):
                    easy_vs_hard(count, g_x, g_o)
                elif (turn_x, turn_o) == ("hard", "medium"):
                    medium_vs_hard(count, g_o, g_x)
                elif (turn_x, turn_o) == ("medium", "hard"):
                    medium_vs_hard(count, g_x, g_o)
                elif turn_x == "user" and turn_o == "medium" or turn_o == "easy" or turn_o == "hard":
                    game_w_comp(turn_o, g_x, g_o)
                elif turn_o == "user" and turn_x == "medium" or turn_x == "easy" or turn_x == "hard":
                    game_w_comp(turn_x, g_o, g_x)

                show_board()
                win_ch.main()
                count += 1

        elif cmd == "exit":
            break
        else:
            print("Bad parameters!")
        reset_board()
        g_resume = True


run()
