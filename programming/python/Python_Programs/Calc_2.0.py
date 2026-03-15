import sys
from PyQt5 import QtCore,QtGui
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit, QLabel
from PyQt5.QtGui import QPalette, QColor, QPixmap, QBrush

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Aidan Calc App')
        self.setLayout(QVBoxLayout())
        self.last_pressed = []

        pixmap = QPixmap("C:/Users/Sh1nO/Documents/Programming/python/Python_Programs/aid.jpg")

        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(pixmap))

        self.setPalette(palette)
        self.setAutoFillBackground(True)
        
        self.input_field = QLineEdit()
        self.input_field.setReadOnly(True)
        self.input_field.setAlignment(QtCore.Qt.AlignRight)
        self.input_field.setText('0')
        self.layout().addWidget(self.input_field)
        
        buttons = [
            ['7', '8', '9', '÷'],
            ['4', '5', '6', '×'],
            ['1', '2', '3', '−'],
            ['0', '00', '.', '+'],
            ['C', '+/-', '=', '%']
        ]
        
        grid_layout = QGridLayout()
        
        for row, button_row in enumerate(buttons):
            for col, button_label in enumerate(button_row):
                button = QPushButton(button_label)
                button.clicked.connect(self.button_clicked)
                button.setObjectName("calculatorButton")
                if button_label in ['÷', '×', '−', '+', '+/-', '=', '%','C']:
                    button.setObjectName("mathButton")
                grid_layout.addWidget(button, row, col)
        
        self.layout().addLayout(grid_layout)
        
        self.current_value = ''
        
        self.setStyleSheet('''
            QPushButton#calculatorButton {
                background-color: #2193F0;
                color: white;
                font-size: 20px;
                padding: 10px;
                border-radius: 22px;
            }
            QLineEdit {
                background-color: #222222;
                color: white;
                font-size: 24px;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton#mathButton {
                background-color: #dddddd;
                color: #FFA500;
                font-size: 20px;
                padding: 10px;
                border-radius: 22px;
            }
            QPushButton#mathButton:hover {
                background-color: #ffffff;
            }
            QPushButton#mathButton:pressed {
                background-color: #777777;
            }
            QPushButton#calculatorButton:hover {
                background-color: #ffb300;
            }

            QPushButton#calculatorButton:pressed {
                background-color: #735a1f;
            }
        ''')
    def symbdup(self,text):
        if text in ['+', '-', '*', '/']:
                
            if len(self.current_value) > 0 and self.current_value[-1] in ['+', '-', '*', '/']:
                self.current_value = self.current_value[:-1] + text
            else:
                self.current_value += text
        else:
            self.current_value += text

        self.input_field.setText(self.current_value)

    def button_clicked(self):
        button = self.sender()
        text = button.text()
        dis_text = self.input_field.text()
        symb = ['+', '-', '*', '/', '%']

        if text == '=':
            try:
                result = eval(self.current_value)
                result = round(result, 6)
                result = "{:.13g}".format(Decimal(str(result)))
                self.input_field.setText(result)
                self.current_value = str(result)
                self.last_pressed = '='
            except (SyntaxError, ZeroDivisionError):
                self.input_field.setText('Error')
                self.current_value = ''
        elif text == 'C':
            self.input_field.clear()
            self.current_value = ''
            self.input_field.setText('0')
            self.last_pressed = []

        elif self.current_value == '0':
            if text != '0' and text != '.':
                self.current_value = text
                self.input_field.setText(text)
        elif self.current_value == '00':
            
            if text != '0':
                self.current_value = text
                self.input_field.setText(text)

        elif self.current_value == '0' or self.current_value == '00':
            self.current_value = text
            self.input_field.setText(text)
        elif self.last_pressed == '=' and text.isnumeric():
            self.input_field.setText(text)
            self.current_value = text
            self.last_pressed = text
        elif text == '÷':
            text = '/'
            self.symbdup(text)
        elif text == '−':
            text = '-'
            self.symbdup(text)
        elif text == '×':
            text = '*'
            self.symbdup(text)
        elif text == '+/-': 
           if self.current_value:
                if self.current_value.startswith('-'):
                    self.current_value = self.current_value[1:]
                else:
                    self.current_value = '-' + self.current_value
                self.input_field.setText(self.current_value)
        elif text == '%':
            text = '/100'
            self.symbdup(text)
        else:
            self.symbdup(text)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
