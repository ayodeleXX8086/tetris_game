from cli_utils import get_input, valid_moves, clear_screen
from game import start_t_move, Board, make_the_board_move, start_1_move, start_L_move


def select_move(index):
    moves = [start_t_move(10), start_1_move(10), start_L_move(10)]
    return moves[index % len(moves)]


def main():
    board = Board(10)
    idx = 0
    move_ = select_move(idx)
    board.make_move(move_)
    while True:
        clear_screen()
        board.display()
        game_over = board.game_over()
        if game_over:
            break
        key = get_input()
        if key == 'exit':
            break
        if key in valid_moves:
            move = make_the_board_move(move_, key)
            if board.validate_movement(move):
                move_ = move
                board.make_move(move)
        board.crusher_board()
        if board.check_for_collision(move_):
            idx += 1
            board.prev_movement = None
            move_ = select_move(idx)
            board.make_move(move_)
    print("The game is Over")


if __name__ == '__main__':
    main()
