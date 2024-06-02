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
    global catfacts
    catfacts = ""
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

        self.Options = QComboBox()
        self.Options.addItems(["Facts","Breeds"])
        layout.addWidget(self.Options)

        label2 = QLabel("Choose how many?")
        layout.addWidget(label2)

        self.qty = QComboBox()
        self.qty.addItems(["1","2","3","4","5"])
        layout.addWidget(self.qty)
       
        self.user_sel_button = QPushButton(text="Submit Selections")
        layout.addWidget(self.user_sel_button)
        self.user_sel_button.clicked.connect(self.call_controller)
                
        label3 = QLabel("Results:")
        layout.addWidget(label3)
        
        self.result0 = QLabel("")
        layout.addWidget(self.result0)

        self.result1 = QLabel("")
        layout.addWidget(self.result1)

        self.result2 = QLabel("")
        layout.addWidget(self.result2)

        self.result3 = QLabel("")
        layout.addWidget(self.result3)

        self.result4 = QLabel("")
        layout.addWidget(self.result4)

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)

    def clear_labels(self):
            self.result0.setText("")
            self.result1.setText("")
            self.result2.setText("")
            self.result3.setText("")
            self.result4.setText("")
            
    def call_controller(self):
        self.clear_labels()
        user_sel1 = self.Options.currentText().lower()
        user_sel2 = self.qty.currentIndex() + 1
        catfacts = controller.catfact(user_sel1, user_sel2)
        catfactslist = catfacts.split('\n')
        x = 0
        for x in range(user_sel2):
            if x == 0:
                self.result0.setText(catfactslist[0])
            if x == 1:
                self.result1.setText(catfactslist[1])
            if x == 2:
                self.result2.setText(catfactslist[2])
            if x == 3:
                self.result3.setText(catfactslist[3])
            if x == 4:
                self.result4.setText(catfactslist[4])    
            x = x+1

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()