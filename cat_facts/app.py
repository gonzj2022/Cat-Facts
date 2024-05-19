import sys
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget
)
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("WikiCats")
        layout = QVBoxLayout()
        widgets = [
            QLabel,
            QComboBox,
            QLabel,
            QSpinBox,
            QPushButton,
            QLCDNumber
        ]
        label1 = QLabel("Would you like to learn about Cats Facts or Breeds?")
        layout.addWidget(label1)

        Options1 = QComboBox()
        Options1.addItems(["Facts","Breeds"])
        layout.addWidget(Options1)

        label2 = QLabel("Choose how many?")
        layout.addWidget(label2)

        Options2 = QComboBox()
        Options2.addItems(["1","2","3","4","5"])
        layout.addWidget(Options2)

        PB1 = QPushButton(text="Sumbit Selections")
        layout.addWidget(PB1)

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()