import tkinter as tk

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.board = [[' ' for j in range(3)] for i in range(3)]
        self.cells = [[tk.Label(self.window, text=self.board[i][j], font=('Arial', 30), width=3, height=1, bg='white', relief='sunken') for j in range(3)] for i in range(3)]
        [self.cells[i][j].grid(row=i, column=j) and self.cells[i][j].bind('<Button-1>', lambda event, row=i, col=j: self.play_move(row, col)) for i in range(3) for j in range(3)]
        self.current_player = 'X'
        self.player_label = tk.Label(self.window, text=f"Current player: {self.current_player}", font=('Arial', 16))
        self.player_label.grid(row=3, column=0, columnspan=3)
        self.window.mainloop()
    
    def play_move(self, row, col):
        if self.check_win() or self.check_tie():
            return
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.cells[row][col].configure(text=self.current_player, bg='light gray')
            if self.check_win():
                self.player_label.configure(text=f"{self.current_player} wins!")
            elif self.check_tie():
                self.player_label.configure(text="It's a tie!")
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                self.player_label.configure(text=f"Current player: {self.current_player}")
    
    def check_win(self):
        if any(self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ' for i in range(3)) or \
           any(self.board[0][j] == self.board[1][j] == self.board[2][j] != ' ' for j in range(3)) or \
           self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ' or \
           self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        return False
    
    def check_tie(self):
        return all(' ' not in row for row in self.board)

game = TicTacToe()
