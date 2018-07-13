from tkinter import Tk, Label, Button


def victor_screen(player):
        root = Tk()
        root.title('Victory!')
        label = Label(root, text='Player: ' + str(player) + ' Won')
        label.pack()
        button_ok = Button(root, text='Ok', command=lambda: [root.destroy(), quit()])
        button_ok.pack()
        root.mainloop()


def size_of_board(butt, answer, char, player):
    """Conditions when players can won"""
    if answer == 'SMALL':
        for x, y in enumerate(butt):
            try:
                if butt[x].cget('text') == char and butt[x + 1].cget('text') == char \
                        and butt[x + 2].cget('text') == char:
                    victor_screen(player)
                elif butt[x].cget('text') == char and butt[x + 3].cget('text') == char \
                        and butt[x + 6].cget('text') == char:
                    victor_screen(player)
                    break
                elif butt[x].cget('text') == char and butt[x + 4].cget('text') == char and butt[x + 8].cget(
                        'text') == char:
                    victor_screen(player)
                    break
                elif butt[x + 2].cget('text') == char and butt[x + 4].cget('text') == char and butt[x + 6].cget(
                        'text') == char:
                    victor_screen(player)
                    break
            except IndexError:
                return
    elif answer == 'MEDIUM':
        for x, y in enumerate(butt):
            try:
                if butt[x].cget('text') == char and butt[x + 1].cget('text') == char \
                        and butt[x + 2].cget('text') == char and butt[x+3].cget('text') == char:
                    victor_screen(player)
                    break
                elif butt[x].cget('text') == char and butt[x + 4].cget('text') == char \
                        and butt[x + 8].cget('text') == char and butt[x+12].cget('text') == char:
                    victor_screen(player)
                    break
                elif butt[x].cget('text') == char and butt[x + 5].cget('text') == char \
                        and butt[x + 10].cget('text') == char and butt[x+15].cget('text') == char:
                    victor_screen(player)
                    break
                elif butt[x + 3].cget('text') == char and butt[x + 6].cget('text') == char \
                        and butt[x + 9].cget('text') == char and butt[x+12].cget('text') == char:
                    victor_screen(player)
                    break
            except IndexError:
                return

    elif answer == 'BIG':
        for x, y in enumerate(butt):
            try:
                if butt[x].cget('text') == char and butt[x + 1].cget('text') == char \
                        and butt[x + 2].cget('text') == char and butt[x + 3].cget('text') == char\
                        and butt[x + 4].cget('text') == char:
                    victor_screen(player)
                    break
                elif butt[x].cget('text') == char and butt[x + 5].cget('text') == char \
                        and butt[x + 10].cget('text') == char and butt[x + 15].cget('text') == char \
                        and butt[x + 20].cget('text') == char:
                    victor_screen(player)
                    break
                elif butt[x].cget('text') == char and butt[x + 6].cget('text') == char \
                        and butt[x + 12].cget('text') == char and butt[x+18].cget('text') == char \
                        and butt[x + 24].cget('text') == char:
                    victor_screen(player)
                    break
                elif butt[x + 4].cget('text') == char and butt[x + 8].cget('text') == char \
                        and butt[x + 12].cget('text') == char and butt[x+16].cget('text') == char \
                        and butt[x + 20].cget('text') == char:
                    victor_screen(player)
                    break
            except IndexError:
                return