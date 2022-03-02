import sys
import os

# https://github.com/ColinDuquesnoy/QDarkStyleSheet
import qdarkstyle

from MainWindowLogic import MainWindowLogic
from MainWindowViewModel import MainWindowViewModel

# set the environment variable to use a specific wrapper
# it can be set to pyqt, pyqt5, pyside or pyside2 (not implemented yet)
# you do not need to use QtPy to set this variable
os.environ['QT_API'] = 'pyqt5'

# import from QtPy instead of doing it directly
# note that QtPy always uses PyQt5 API
from qtpy import QtWidgets;

def main():
    app = QtWidgets.QApplication(sys.argv)
    vm = MainWindowViewModel()
    ui = MainWindowLogic(vm)

    # setup stylesheet
    # the default system in qdarkstyle uses qtpy environment variable
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    # ui.showMaximized()
    ui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
