from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PyQt5.QtCore import QSize, Qt

import sys

from MainWindowLogic import MainWindowLogic;
from MainWindowViewModel import MainWindowViewModel;


def main():
    app = QApplication(sys.argv)
    vm = MainWindowViewModel();
    ui = MainWindowLogic(vm);
    # ui.showMaximized()
    ui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
