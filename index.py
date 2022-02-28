from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton;
from PyQt5.QtCore import QSize, Qt;

import sys;

from Controller import Controller;

def main():
    app = QApplication(sys.argv);
    ui = Controller();
    # ui.showMaximized()
    ui.show();
    sys.exit(app.exec_());

if __name__ == "__main__":
    main();