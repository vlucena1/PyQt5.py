import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QMessageBox, QLabel, QHBoxLayout, QWidget

app = QApplication(sys.argv)
button = QPushButton('Button 0')
button1 = QPushButton('Button 1')
button2 = QPushButton('Button 2')
label = QLabel('Press a button')

# Define the slot functions
def on_button_clicked():
    QMessageBox.information(button, 'Message', 'Button clicked!')

def on_button1_clicked():
   QMessageBox.information(button, 'Message', 'Button 1 clicked!')

def on_button2_clicked():
  QMessageBox.information(button, 'Message', 'Button 2 clicked!')

# Connect the clicked signals to the slot functions
button.clicked.connect(on_button_clicked)
button1.clicked.connect(on_button1_clicked)
button2.clicked.connect(on_button2_clicked)

# Create a horizontal layout and add the widgets
layout = QHBoxLayout()
layout.addWidget(label)
label.setStyleSheet('font-size: 32px; color: blue;')
layout.addWidget(button)
layout.addWidget(button1)
layout.addWidget(button2)


# Create a widget to hold the layout

widget = QWidget()
widget.setLayout(layout)
button.show()
widget.show()

# Run the application loop
sys.exit(app.exec_())


