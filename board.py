from tkinter import Tk, Label, Button, Entry, StringVar, TclError

from board_size import size_of_board
from players import Players

'Make clicked buttons show X or O'
'Predefined sizes : 3x3, 4x4, 5x5'


class XOBoard:
    def __init__(self):
        self.root = Tk()
        self.label = Label(self.root, text='How big board should be?:\t Small, Medium, Big')
        self.label.grid(row=0, column=0)
        self.entry = Entry(self.root)
        self.entry.grid(row=1, column=0)
        self.button = Button(self.root, text='Ok', command=lambda: [self.get_value(), self.root.destroy()])
        self.button.grid(row=2, column=0)
        self.id_buttons = {}
        self.id_label = None
        self.size = {"SMALL": '3x3', "MEDIUM": '4x4', "BIG": '5x5'}
        self.answer = None
        self.x_length = 0
        self.y_length = 0
        self.val_players = Players()
        self.char_value = list(self.val_players.players.values())
        self.player_value = list(self.val_players.players.keys())
        self.player_number = 1
        self.root.mainloop()

    def error_window(self):
        """Error Window will show up when input of board size is invalid"""
        f = Tk()
        label = Label(f, text='Error, There is no such size as ' + self.answer)
        label.grid(row=0, column=0)
        button = Button(f, text='Ok', command=lambda: [quit()])
        button.grid(row=1, column=0)
        f.mainloop()

    def get_value(self):
        """Get value of entry"""
        self.answer = self.entry.get()

    def __board_size(self):
        """Convert answer to upper; compare answer to fixed list with sizes;
        Assign x, y values to variables"""
        try:
            self.answer = self.answer.upper()

        except AttributeError:
            return

        val_ans = ''

        for keys, value in self.size.items():
            if self.answer == keys:
                val_ans = value

        try:
            val_ans = val_ans.split('x')
            self.x_length = int(val_ans[0])
            self.y_length = int(val_ans[1])

        except ValueError:

            self.error_window()

    def check_condition(self):
        """Check if player won"""
        all_info = self.id_buttons.items()
        butt = []

        for x, y in all_info:
            butt.append(x)

        size_of_board(butt, self.answer, self.char_value[0], self.player_number)

    def on_click(self, x, y, label_text):
        """Check condition when clicked on field; Replace coordinates with X and disable clicked Button
        ;Cycle player number"""
        all_info = self.id_buttons.items()

        get_coord = str(x) + ' ' + str(y)

        for x, y in all_info:
            if get_coord in y[2]:
                try:
                    x.config(text=self.char_value[0], state='disabled', font=('Arial', '9'))  # Wstawienie chara

                    self.check_condition()  # Sprawdzenie warunku

                    self.player_number = self.val_players.cycle_player(int(label_text.get()))
                    label_text.set(str(self.player_number))
                    self.id_label.config(text='Player:\t' + label_text.get()) # zmiana nr playera

                    self.char_value = self.val_players.cycle_char(self.char_value[0])  # Zmiana chara
                except TclError:
                    return

    def generate_game_board(self):
        """Generate board"""
        self.__board_size()
        root = Tk()

        button_text = StringVar()
        label_text = StringVar()
        label_text.set(str(self.player_value[0]))

        label = Label(root, text='Tic Tac Toe')
        label.grid(row=0, column=0)

        id_label = Label(root, text='Player:\t' + label_text.get())
        id_label.grid(row=1, column=0)

        for rows in range(0, self.x_length):  # Horizontal
            for columns in range(0, self.y_length):  # Vertical
                button_text.set(str(rows) + ' ' + str(columns))

                """Assign object button to id_button; Add id to a list"""
                id_button = Button(root, width=10, height=5, text=button_text.get(),
                command=lambda x=rows, y=columns: self.on_click(x, y, label_text))
                id_button.grid(row=rows + 5, column=columns + 5)

                self.id_buttons[id_button] = rows, columns, button_text.get()

        self.id_label = id_label
        root.mainloop()


if __name__ == '__main__':
    f = XOBoard()
    f.generate_game_board()
