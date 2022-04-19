import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from sympy import true

app = QApplication(sys.argv)
#Window
window = QWidget()
window.setWindowTitle('Backslash To Slash Program')
window.setGeometry(100,100,400,200)
window.move(60,15)

#Functions
def backslash_to_slashfn(back_slash_path):
  text = "%s" %(back_slash_path)
  Second_Input.setText(text.replace("\\",R"/"))
  print(Second_Input.text())

#Elements
First_input_Msg = QLabel('<h4>Text To Transform:</h4>', parent=window)
First_input_Msg.move(40,72)
Second_Input_Msg = QLabel('<h4>Transformed Text:</h4>', parent=window)
Second_Input_Msg.move(40,113)
First_Input = QLineEdit(parent=window)
First_Input.move(150,70)
Second_Input = QLineEdit(parent=window)
Second_Input.move(150,110)
Submit_Text_Btn = QPushButton("Submit", parent=window)
Submit_Text_Btn.move(290,68)
Submit_Text_Btn.clicked.connect(lambda: backslash_to_slashfn(First_Input.text()))

#Show Window
window.show()




sys.exit(app.exec_())
