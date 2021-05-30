from cli_utils import get_input, valid_moves, clear_screen
from game import start_t_move, Board, make_the_board_move

board = Board(10)
def coroutine_decorator(func):
    def coroutine_args(*args, **kwargs):
        while True:
            pass

def validate_move(coroutine):
    try:

        board.validate_movement()
    except GeneratorExit:
        coroutine.close()
        print("Validate Move")

def draw(coroutine):
    print("Hey Draw")
    try:
        while True:
            coroutine.send('draw')
            res = (yield 'draw')
            print(f"I'm drawing i received this event {res}")
    except GeneratorExit:
        coroutine.close()
        print('close draw')

def make_move(coroutine):
    try:
        while True:
            coroutine.send('crush')
            res = (yield 'make moved')
            print(f"I'm making move i received this event {res}")
    except GeneratorExit:
        coroutine.close()
        print('close make_move')

def crush_board():
    try:
        while True:
            res = (yield 'crushed')
            print(f"I'm crushing board I received this event {res}")
    except GeneratorExit:
        print('close crush_board')

# def test():
#     c = crush_board()
#     next(c)
#     m = make_move(c)
#     next(m)
#     d = draw(m)
#     next(d)
#     i=0
#     t_move = start_t_move(10)
#     while i < 4:
#         key = get_input()
#         if key in valid_moves:
#             res = d.send(f'draw {i}')
#         print(f"Response {res} {i}")
#         i += 1
#     d.close()
# test()

def main():
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
            move = make_the_board_move(t_move,key)
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