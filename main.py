from cli_utils import get_input, valid_moves, clear_screen
from game import start_t_move, Board, make_the_board_move


def main():
    board = Board(10)
    t_move = start_t_move(10)
    board.make_move(t_move)
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
            move = make_the_board_move(t_move, key)
            if board.validate_movement(move):
                t_move = move
                board.make_move(move)
        board.crusher_board()
        if board.check_for_collision(t_move):
            board.prev_movement = None
            t_move = start_t_move(10)
            board.make_move(t_move)
    print("The game is Over")


if __name__ == '__main__':
    main()
