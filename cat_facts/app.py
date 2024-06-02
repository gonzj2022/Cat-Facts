import sys, controller, random
from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QLabel,
    QMainWindow,
    QPushButton,
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
      
        #Question Label settings
        question = QLabel("Would you like to learn about Cats Facts or Breeds?")
        fontquestion = question.font()
        fontquestion.setPointSize(15)
        question.setFont(fontquestion)
        layout.addWidget(question)

        #Options Dropdown settings
        self.Options = QComboBox()
        self.Options.addItems(["Facts","Breeds"])
        fontoptions = self.Options.font()
        fontoptions.setPointSizeF(13)
        self.Options.setFont(fontoptions)
        layout.addWidget(self.Options)

        #Quantity Label settings
        quantity = QLabel("Choose how many?")
        fontquantity = quantity.font()
        fontquantity.setPointSize(15)
        quantity.setFont(fontquantity)
        layout.addWidget(quantity)

        #Quantity Dropdown settings
        self.qty = QComboBox()
        self.qty.addItems(["1","2","3","4","5"])
        fontqty = self.qty.font()
        fontqty.setPointSizeF(13)
        self.qty.setFont(fontqty)
        layout.addWidget(self.qty)
       
        #Submit Button settings
        self.submit_button = QPushButton(text="Submit Selections")
        fontbutton = self.submit_button.font()
        fontbutton.setPointSizeF(13)
        self.submit_button.setFont(fontbutton)
        layout.addWidget(self.submit_button)
        self.submit_button.clicked.connect(self.call_controller)
                
        #Results Label settings
        results = QLabel("Results:")
        fontresults = results.font()
        fontresults.setPointSize(13)
        results.setFont(fontresults)
        layout.addWidget(results)
        
        #Output Labels settings
        self.result0 = QLabel("")
        self.result0.setWordWrap(True)
        fontresult0 = self.result0.font()
        fontresult0.setPointSize(15)
        self.result0.setFont(fontresult0)
        layout.addWidget(self.result0)

        self.result1 = QLabel("")
        layout.addWidget(self.result1)
        fontresult1 = self.result1.font()
        fontresult1.setPointSize(15)
        self.result1.setFont(fontresult1)        
        self.result1.setWordWrap(True)

        self.result2 = QLabel("")
        layout.addWidget(self.result2)
        fontresult2 = self.result2.font()
        fontresult2.setPointSize(15)
        self.result2.setFont(fontresult2)        
        self.result2.setWordWrap(True)

        self.result3 = QLabel("")
        layout.addWidget(self.result3)
        fontresult3 = self.result3.font()
        fontresult3.setPointSize(15)
        self.result3.setFont(fontresult3)        
        self.result3.setWordWrap(True)

        self.result4 = QLabel("")
        layout.addWidget(self.result4)
        fontresult4 = self.result4.font()
        fontresult4.setPointSize(15)
        self.result4.setFont(fontresult4)        
        self.result4.setWordWrap(True)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def clear_results(self):
            self.result0.setText("")
            self.result1.setText("")
            self.result2.setText("")
            self.result3.setText("")
            self.result4.setText("")
            
    def call_controller(self):
        #clear labels after each submit
        self.clear_results()
        user_sel1 = self.Options.currentText().lower()
        #increase value by 1 since index starts with 0
        user_sel2 = self.qty.currentIndex() + 1
        if user_sel1 == "facts":
            for x in range(user_sel2):
                catfacts = controller.catfact(user_sel1)
                if x == 0:
                    self.result0.setText("1.  " + catfacts)
                if x == 1:
                    self.result1.setText("2.  " + catfacts)
                if x == 2:
                    self.result2.setText("3.  " + catfacts)
                if x == 3:
                    self.result3.setText("4.  " + catfacts)
                if x == 4:
                    self.result4.setText("5.  " + catfacts)    
                x = x+1
        if user_sel1 == "breeds":
            catfacts = controller.catfact(user_sel1)
            catfactslist = catfacts.split('\n')
            for x in range(user_sel2):
                if x == 0:
                    self.result0.setText("1.  " + random.choice(catfactslist))
                if x == 1:
                    self.result1.setText("2.  " + random.choice(catfactslist))
                if x == 2:
                    self.result2.setText("3.  " + random.choice(catfactslist))
                if x == 3:
                    self.result3.setText("4.  " + random.choice(catfactslist))
                if x == 4:
                    self.result4.setText("5.  " + random.choice(catfactslist))    
                x = x+1

width = 600; height = 900
app = QApplication(sys.argv)
w = MainWindow()
w.resize(width,height)
w.show()
app.exec()