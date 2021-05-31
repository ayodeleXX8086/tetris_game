from typing import Optional, List


class Movement:
    def __init__(self,
                 points: Optional[List] = None,
                 space_length: int = 3):
        self.space_length = space_length
        self.points = points

    def make_ninety_degree(self):
        """
        This moving ninety degree in clockwise
        :return: self
        """

        min_horizon = min((j for i, j in self.points))
        min_vertical = min((i for i, j in self.points))

        matrix = [[None] * (self.space_length) for _ in range(self.space_length)]
        sorted_lst = sorted(self)
        for value in sorted_lst:
            matrix[value[0] - min_vertical][value[1] - min_horizon] = value
        matrix.reverse()
        for i in range(self.space_length):
            for j in range(i + 1, self.space_length):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        points = []
        for i in range(self.space_length):
            for j in range(self.space_length):
                if matrix[i][j]:
                    points.append((i + min_vertical, j + min_horizon))
        return Movement(points=points)

    def move_left(self):
        points = [tuple([point[0], point[1] - 1]) for point in self.points]
        return Movement(points=points)

    def move_right(self):
        points = [tuple([point[0], point[1] + 1]) for point in self.points]
        return Movement(points=points)

    def move_bottom(self):
        points = [tuple([point[0] + 1, point[1]]) for point in self.points]
        return Movement(points=points)

    def __iter__(self):
        for points in self.points:
            yield points

    def __str__(self):
        return f"Points {sorted(self.points)}"


class Board:
    def __init__(self, length):
        self.board = [[False] * length for _ in range(length)]
        self.length = length
        self.prev_movement = None

    def validate_movement(self, movement: Movement) -> bool:
        for move in movement:
            if (move[0] < 0 or move[0] >= self.length or move[1] < 0 or move[1] >= self.length):
                return False
        return True

    def make_move(self, movement: Movement):
        if self.prev_movement:
            for move in self.prev_movement:
                self.board[move[0]][move[1]] = False
        for move in movement:
            self.board[move[0]][move[1]] = True
        self.prev_movement = movement

    def check_for_collision(self, movement: Movement):
        sorted_move = sorted(movement, key=lambda x: x[0])
        filtered_move = [mv for mv in sorted_move if mv[0] == sorted_move[-1][0]]
        for move in filtered_move:
            if self._check_collision_recursion(move[0] + 1, move[1], set()):
                return True
        return False

    def _check_collision_recursion(self, i, j, cache):
        if self.length <= i:
            return True
        if j < 0 or j >= self.length:
            return False
        if not self.board[i][j]:
            return False
        cache.add((i, j))
        for x, y in [(0, -1), (1, 0), (0, 1)]:
            if (not (x + i, j + y) in cache) and self._check_collision_recursion(i + x, j + y, cache):
                return True
        return False

    def crusher_board(self):
        point = 0
        while any([all(self.board[idx]) for idx in range(0, self.length)[::-1]]):
            self.board.pop(-1)
            self.board.insert(0, [False for _ in range(self.length)])
            point += 1
        return point

    def game_over(self):
        for i in range(self.length):
            res = self._check_collision_recursion(0, i, set())
            if res:
                return True
        return False

    def display(self):
        # Draws the contents of the board with a border around it.
        board_border = "".join(["*" for _ in range(self.length + 2)])
        print(board_border)
        for y in range(self.length):
            line = "|"
            for x in range(self.length):
                line += ("#" if self.board[y][x] else " ")
            line += "|"
            print(line)
        print(board_border)


def start_t_move(length):
    mid = (length - 1) // 2
    points = [(0, mid - 1), (0, mid), (0, mid + 1), (0, mid), (1, mid)]
    t_movement = Movement(points=points)
    return t_movement


def start_1_move(length):
    mid = (length - 1) // 2
    points = [(0, mid), (1, mid), (2, mid)]
    movement_1 = Movement(points=points)
    return movement_1

def start_L_move(length):
    mid = (length-1)//2
    points = [(0,mid),(1,mid),(2,mid),(2,mid+1)]
    movement_L = Movement(points=points)
    return movement_L

def make_the_board_move(movement, move):
    if move == 'up':
        return movement.make_ninety_degree()
    elif move == 'down':
        return movement.move_bottom()
    elif move == 'right':
        return movement.move_right()
    elif move == 'left':
        return movement.move_left()
    else:
        Exception()
