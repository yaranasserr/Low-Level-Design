# Problem: Design Tic-Tac-Toe

Design a class `TicTacToe` that allows players to play a game of Tic-Tac-Toe on an `n x n` board. The game has two players, designated as player 1 and player 2, and they take turns making moves on the board.

The class should support the following functions:

- **`TicTacToe(int n)`** — Initializes the object with a board size of `n x n`.
- **`int move(int row, int col, int player)`** — Indicates that the player with ID `player` (1 or 2) makes a move at the cell `(row, col)` of the board.
  - Returns `0` if there is no winner after the move.
  - Returns `1` if player 1 wins.
  - Returns `2` if player 2 wins.
  - It is guaranteed that the move is valid and the cell `(row, col)` is empty before the move.

