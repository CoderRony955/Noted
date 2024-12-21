from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QMessageBox, QVBoxLayout, QMessageBox, QMainWindow, QTextEdit, QTabWidget, QFileDialog
import sys
from PyQt6.QtGui import QFontDatabase


class fonts(QMainWindow):
    def __init__(self):
        super().__init__()
        self.centralWidget = QWidget()
        self.setWindowTitle("Fonts")
       

        self.text = QTextEdit()
        self.text.setPlaceholderText("Fonts")

        layout = QVBoxLayout()
        layout.addWidget(self.text)

        self.centralWidget.setLayout(layout)
        self.setCentralWidget(self.centralWidget)

    def Fonts(self):
        all_fonts = QFontDatabase.families()
        font_list = "\n".join(all_fonts) 
        self.text.setText(font_list)  # Display the font names in the text widget



if __name__ == "__main__":
    app = QApplication(sys.argv)
    fots = fonts()
    fots.show()
    fots.Fonts()
    sys.exit(app.exec())
