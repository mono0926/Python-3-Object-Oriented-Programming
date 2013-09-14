from PyQt4 import QtGui
import random

app = QtGui.QApplication([])

choices = ["Rock", "Paper", "Scissors"]

class RockPaperScissorsWidget(QtGui.QWidget):
    def __init__(self):
        super().__init__()
        rock = RPSButton("Rock", self)
        paper = RPSButton("Paper", self)
        scissors = RPSButton("Scissors", self)
        for button in (rock, paper, scissors):
            button.resize(100, 100)
        rock.move(0,0)
        paper.move(0,100)
        scissors.move(0,200)
        self.response = QtGui.QLabel("", self)
        self.response.setGeometry(110, 0, 200, 300)

class RPSButton(QtGui.QPushButton):
    def mousePressEvent(self, event):
        computer_choice = random.choice(choices)
        user_choice = self.text()

        comp_idx = choices.index(computer_choice)
        user_idx = choices.index(user_choice)

        message = {
                0: 'Tied',
                1: 'Computer Wins',
                2: 'You Win'}[(comp_idx - user_idx + 3) % 3]


        self.parent().response.setText("You chose {0}<br />"
                "Computer chose {1}<br />"
                "{2}".format(user_choice, computer_choice, message))


window = RockPaperScissorsWidget()
window.show()
app.exec_()
