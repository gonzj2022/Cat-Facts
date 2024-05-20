import sys, controller
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

        self.Options1 = QComboBox()
        self.Options1.addItems(["Facts","Breeds"])
        layout.addWidget(self.Options1)

        label2 = QLabel("Choose how many?")
        layout.addWidget(label2)

        self.Options2 = QComboBox()
        self.Options2.addItems(["1","2","3","4","5"])
        layout.addWidget(self.Options2)

        self.PB1 = QPushButton(text="Sumbit Selections")
        layout.addWidget(self.PB1)
        self.PB1.clicked.connect(self.call_controller)

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)

    def call_controller(self):
        user_sel1 = self.Options1.currentIndex()
        user_sel2 = self.Options2.currentIndex() + 1
        controller.catfact(user_sel1, user_sel2)

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()