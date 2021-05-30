from unittest import TestCase

from game import Movement, Board


class MovementUnitTest(TestCase):
    def setUp(self):
        self.t_movement = Movement(points=[(0, 3), (0, 4), (0, 5), (1, 4)])

    def test_ninety_degree(self):
        movement = self.t_movement.make_ninety_degree()
        expected_result = sorted([(0, 5), (1, 4), (1, 5), (2, 5)])
        result = sorted(list(movement))
        self.assertEqual(result, expected_result)

    def test_move_left(self):
        movement = self.t_movement.move_left()
        expected_result = sorted([(0, 2), (0, 3), (0, 4), (1, 3)])
        result = sorted(list(movement))
        self.assertEqual(result, expected_result)

    def test_move_right(self):
        movement = self.t_movement.move_right()
        expected_result = sorted([(0, 4), (0, 5), (0, 6), (1, 5)])
        result = sorted(list(movement))
        self.assertEqual(result, expected_result)

    def test_move_bottom(self):
        movement = self.t_movement.move_bottom()
        expected_result = sorted([(1, 3), (1, 4), (1, 5), (2, 4)])
        result = sorted(list(movement))
        self.assertEqual(result, expected_result)


class TetrisBoardUnitTest(TestCase):
    def setUp(self):
        self.board = Board(10)

    def test_fake_move_on_board(self):
        movement = Movement(points=[(0, 8), (0, 9), (0, 10), (1, 9)])
        result = self.board.validate_movement(movement)
        self.assertFalse(result)

    def test_board_collision(self):
        movement = Movement(points=[(9, 3), (9, 4), (9, 5), (8, 4)])
        result = self.board.check_for_collision(movement)
        self.assertTrue(result)

    def test_crusher_board(self):
        movement = Movement(points=[(9, 0), (9, 1), (9, 2), (8, 2)])
        self.board.make_move(movement)
        self.board.prev_movement = None
        movement = Movement(points=[(9, 3), (9, 4), (9, 5), (8, 4)])
        self.board.make_move(movement)
        self.board.prev_movement = None
        movement = Movement(points=[(9, 6), (9, 7), (9, 8), (8, 7)])
        self.board.make_move(movement)
        self.board.prev_movement = None
        movement = Movement(points=[(9, 9), (8, 9), (7, 9), (8, 8)])
        self.board.make_move(movement)
        self.board.prev_movement = None
        point = self.board.crusher_board()
        self.assertEqual(point, 1)

    def test_game_over_board(self):
        movement = Movement(points=[(9, 4), (8, 3), (8, 4), (8, 5)])
        self.board.make_move(movement)
        self.board.prev_movement = None
        movement = Movement(points=[(7, 4), (6, 3), (6, 4), (6, 5)])
        self.board.make_move(movement)
        self.board.prev_movement = None
        movement = Movement(points=[(5, 4), (4, 3), (4, 4), (4, 5)])
        self.board.make_move(movement)
        self.board.prev_movement = None
        movement = Movement(points=[(3, 4), (2, 3), (2, 4), (2, 5)])
        self.board.make_move(movement)
        self.board.prev_movement = None
        movement = Movement(points=[(1, 4), (0, 3), (0, 4), (0, 5)])
        self.board.make_move(movement)
        self.board.prev_movement = None
        result = self.board.game_over()
        self.assertTrue(result)
