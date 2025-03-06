import unittest
from collections import defaultdict

class TicTacToe:
    def __init__(self, n: int):
        self.rows = defaultdict(int)
        self.cols=  defaultdict(int)
        self.left_diag = 0 
        self.right_diag = 0
        self.n = n

       
    def move(self, row: int, col: int, player: int) -> int:
        number = 0 
        number=1 if player==1 else -1
        self.rows[row]+=number
        self.cols[col]+=number
        #left diagonal
        if row==col:
            self.left_diag+=number
        #right diagonal
        if row+col==self.n-1:
            self.right_diag+=number
        if abs(self.rows[row])==self.n or abs(self.cols[col])==self.n or abs(self.left_diag)==self.n or abs(self.right_diag)==self.n:
            return player
        return 0
        

class TestTicTacToe(unittest.TestCase):
    def test_game(self):
        toe = TicTacToe(3)
        self.assertEqual(toe.move(0, 0, 1), 0)
        self.assertEqual(toe.move(0, 2, 2), 0)
        self.assertEqual(toe.move(2, 2, 1), 0)
        self.assertEqual(toe.move(1, 1, 2), 0)
        self.assertEqual(toe.move(2, 0, 1), 0)
        self.assertEqual(toe.move(1, 0, 2), 0)
        self.assertEqual(toe.move(2, 1, 1), 1)  # Player 1 wins


if __name__ == "__main__":
    unittest.main()
