from PyQt4 import QtGui

app = QtGui.QApplication([])

class EmptyWidget(QtGui.QWidget):
    pass

window = EmptyWidget()
window.show()
app.exec_()
