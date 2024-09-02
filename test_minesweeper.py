import pytest
import minesweeper

def test_module_exists():
    assert minesweeper

def test_place_mines():
    game = minesweeper.Minesweeper(3, 3, 2)
    game.place_mines()
    # TODO : Add assertions
    assert len(game.mines) == 2

 def place_mines(self):
        while len(self.mines) < self.num_mines:
            r,c = random.randint(0, self.rows - 1), random.randint(0, self.cols - 1)
            if (r, c) not in self.mines:
                self.mines.add((r, c))
                self.board[r][c] =  '💣'
        
        for r, c in self.mines:
            for i in range(r-1, r+2):
                for j in range(c-1, c+2):
                    if 0 <= i < self.rows and 0 <= j < self.cols and self.board[i][j] != '💣':
                        if self.board[i][j] == '':
                            self.board[i][j] = 1
                        else:
                            self.board[i][j] += 1
def test_reveal():
    import random 
    random.seed(0)
    game = minesweeper.Minesweeper(3, 3, 2)
    game.place_mines()
    game.reveal(2, 2)
    # TODO : Add assertions
    assert game.revealed == {(2, 2)}

def test_fail():
    assert False