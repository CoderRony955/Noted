from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QHBoxLayout,
    QMessageBox,
    QVBoxLayout,
    QMessageBox,
    QMainWindow,
    QTextEdit,
    QTabWidget,
    QFileDialog,
    QSplashScreen

)
from PyQt6.QtGui import QIcon, QFont, QDragEnterEvent, QDropEvent, QPixmap
from PyQt6.QtCore import Qt, QSize, QTimer
import os
import sys

# ****     **   *******   ********** ******** *******
# /**/**   /**  **/////** /////**/// /**///// /**////**
# /**//**  /** **     //**    /**    /**      /**    /**
# /** //** /**/**      /**    /**    /******* /**    /**
# /**  //**/**/**      /**    /**    /**////  /**    /**
# /**   //****//**     **     /**    /**      /**    **
# /**    //*** //*******      /**    /********/*******
# //      ///   ///////       //     //////// ///////


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
    abs_path = os.path.join(base_path, 'icons', relative_path)
    print(f"Resolved path for {relative_path}: {abs_path}")  # Debugging
    return abs_path


class ResourceManager:
    def __init__(self):
        self.images = {
            'Noted_s_icon': resource_path('Noted_S.png'),
            'zoom_in_icon': resource_path('zoom_in_magnifier.png'),
            'zoom_out_icon': resource_path('zoom_out_magnifier.png'),

        }

    def get_image_path(self, name):
        return self.images[name]


class mainwin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.centralWidget = QWidget()
        self.resources = ResourceManager()
        self.setWindowTitle("Noted Silver")
        self.setGeometry(300, 300, 1000, 650)
        self.setWindowIcon(
            QIcon(self.resources.get_image_path('Noted_s_icon')))
        self.setObjectName("Noted")

        self.current_theme = 'dark'
        self.setStyleSheet(self.to_dark_theme())

        setmenu = self.menuBar()
        setmenu.setObjectName("setmenu")
        font = QFont()
        font.setFamily("monospace")
        setmenu.setFont(font)

        File = setmenu.addMenu('File')

        open_file = File.addAction("Open")
        open_file.setShortcut("shift+o")
        open_file.triggered.connect(self.open_file_dialog)

        save = File.addAction("Save")
        save.setShortcut("ctrl+s")
        save.triggered.connect(self.save_file)

        save_as = File.addAction("Save As")
        save_as.setShortcut("ctrl+shift+s")
        save_as.triggered.connect(self.save_as)

        PT = setmenu.addMenu("Productive tools")

        calculator = PT.addAction("Calculator")
        calculator.setShortcut("shift+c")
        calculator.triggered.connect(self.open_calculator)

        wordpad = PT.addAction("Wordpad")
        wordpad.setShortcut("shift+w")
        wordpad.triggered.connect(self.open_wordpad)

        clock = PT.addAction("Clock")
        clock.setShortcut("shift+k")
        clock.triggered.connect(self.open_clock)

        settings = PT.addAction("Settings")
        settings.setShortcut("shift+s")
        settings.triggered.connect(self.open_settings)

        ST = setmenu.addMenu("System tools")
        terminal = ST.addAction("Terminal")
        terminal.setShortcut("shift+t")
        terminal.triggered.connect(self.open_terminal)

        registery_editor = ST.addAction("Registry Editor")
        registery_editor.setShortcut("shift+r")
        registery_editor.triggered.connect(self.open_registery_editor)

        win_sec = ST.addAction("Windows Security")
        win_sec.setShortcut("alt+w")
        win_sec.triggered.connect(self.open_win_sec)

        task_manager = ST.addAction("Task Manager")
        task_manager.setShortcut("alt+t")
        task_manager.triggered.connect(self.open_task_manager)

        resource_monitor = ST.addAction("Resource monitor")
        resource_monitor.setShortcut("alt+r")
        resource_monitor.triggered.connect(self.open_Resource_monitor)

        perf_monitor = ST.addAction("Performance monitor")
        perf_monitor.setShortcut("alt+p")
        perf_monitor.triggered.connect(self.open_performance_monitor)

        GT = setmenu.addMenu("Graphic tools")
        snipping_tool = GT.addAction("Snipping tool")
        snipping_tool.setShortcut("ctrl+alt+s")
        snipping_tool.triggered.connect(self.open_snipping_tool)

        paint = GT.addAction("Paint")
        paint.setShortcut("ctrl+alt+p")
        paint.triggered.connect(self.open_paint)

        canva = GT.addAction("Canva")
        canva.setShortcut("ctrl+alt+c")
        canva.triggered.connect(self.open_canva)

        MST = setmenu.addMenu("MS office tools")
        ms_word = MST.addAction("MS Word")
        ms_word.setShortcut("ctrl+alt+w")
        ms_word.triggered.connect(self.open_ms_word)

        ms_excel = MST.addAction("MS Excel")
        ms_excel.setShortcut("ctrl+alt+x")
        ms_excel.triggered.connect(self.open_ms_excel)

        ms_access = MST.addAction("MS Access")
        ms_access.setShortcut("ctrl+alt+a")
        ms_access.triggered.connect(self.open_ms_access)

        ms_powerpoint = MST.addAction("MS Powerpoint")
        ms_powerpoint.setShortcut("ctrl+shift+p")
        ms_powerpoint.triggered.connect(self.open_ms_powerpoint)

        ms_outlook = MST.addAction("MS Outlook")
        ms_outlook.setShortcut("ctrl+alt+o")
        ms_outlook.triggered.connect(self.open_ms_outlook)

        ms_teams = MST.addAction('Ms Teams')
        ms_teams.setShortcut('ctrl+alt+t')
        ms_teams.triggered.connect(self.open_ms_teams)

        DT = setmenu.addMenu("Developer tools")
        vs = DT.addAction("Visual Studio")
        vs.setShortcut("alt+v+s")
        vs.triggered.connect(self.open_vs)

        vscode = DT.addAction("Visual Studio Code")
        vscode.setShortcut("alt+v+c")
        vscode.triggered.connect(self.open_vscode)

        # main

        self.text_area = QTextEdit()
        self.text_area.setPlaceholderText("Start writing...")
        self.text_area.setObjectName("text_area")
        self.text_area.setAcceptDrops(True)

        self.text_area.dragEnterEvent = self.dragEvent
        self.text_area.dropEvent = self.dropEvent

        # buttons
        copy_button = QPushButton("Copy")
        copy_button.setFixedSize(110, 40)
        copy_button.setCursor(Qt.CursorShape.PointingHandCursor)
        copy_button.setObjectName("copy_button")

        font = QFont()
        font.setFamily('monospace')
        font.setPixelSize(15)
        copy_button.setFont(font)
        copy_button.clicked.connect(self.text_area.copy)

        # cutbutton----------------------------------------
        cut_button = QPushButton("Cut")
        cut_button.setFixedSize(110, 40)
        cut_button.setCursor(Qt.CursorShape.PointingHandCursor)
        cut_button.setObjectName("cut_button")

        font = QFont()
        font.setFamily('monospace')
        font.setPixelSize(15)
        cut_button.setFont(font)
        cut_button.clicked.connect(self.text_area.cut)

        # pastebutton-------------------------------------
        paste_button = QPushButton("Paste")
        paste_button.setFixedSize(110, 40)
        paste_button.setCursor(Qt.CursorShape.PointingHandCursor)
        paste_button.setObjectName("paste_button")

        font = QFont()
        font.setFamily('monospace')
        font.setPixelSize(15)
        paste_button.setFont(font)
        paste_button.clicked.connect(self.text_area.paste)

        # insert plain text button-------------------------------------
        insert_text = QPushButton("Random text")
        insert_text.setFixedSize(110, 40)
        insert_text.setCursor(Qt.CursorShape.PointingHandCursor)
        insert_text.setObjectName("insert_text")

        font = QFont()
        font.setFamily('monospace')
        font.setPixelSize(13)
        insert_text.setFont(font)
        insert_text.clicked.connect(self.plain_random_text)

        # to html button-------------------------------------
        to_html = QPushButton("To HTML")
        to_html.setFixedSize(110, 40)
        to_html.setCursor(Qt.CursorShape.PointingHandCursor)
        to_html.setObjectName("to_html")

        font = QFont()
        font.setFamily('monospace')
        font.setPixelSize(15)
        to_html.setFont(font)
        to_html.clicked.connect(self.to_html_format)

        # undobutton-------------------------------------------
        undo_button = QPushButton("Undo")
        undo_button.setFixedSize(110, 40)
        undo_button.setCursor(Qt.CursorShape.PointingHandCursor)
        undo_button.setObjectName("undo_button")

        font = QFont()
        font.setFamily('monospace')
        font.setPixelSize(15)
        undo_button.setFont(font)
        undo_button.clicked.connect(self.text_area.undo)

        # redobutton------------------------------------------
        redo_button = QPushButton("Redo")
        redo_button.setFixedSize(110, 40)
        redo_button.setCursor(Qt.CursorShape.PointingHandCursor)
        redo_button.setObjectName("redo_button")

        font = QFont()
        font.setFamily('monospace')
        font.setPixelSize(15)
        redo_button.setFont(font)
        redo_button.clicked.connect(self.text_area.redo)

        # clearbutton--------------------------------------
        clear_button = QPushButton("Clear")
        clear_button.setFixedSize(110, 40)
        clear_button.setCursor(Qt.CursorShape.PointingHandCursor)
        clear_button.setShortcut("alt+c")
        clear_button.setObjectName("clear_button")

        font = QFont()
        font.setFamily('monospace')
        font.setPixelSize(15)
        clear_button.setFont(font)
        clear_button.clicked.connect(self.text_area.clear)

        # zoom in button----------------------------------------
        zoom_in_button = QPushButton()
        zoom_in_button.setFixedSize(50, 40)
        zoom_in_button.setCursor(Qt.CursorShape.PointingHandCursor)
        zoom_in_button.setObjectName("zoom_in_button")
        zoom_in_button.setShortcut("ctrl+up")
        zoom_in_button.setIcon(QIcon(
            self.resources.get_image_path('zoom_in_icon')))
        zoom_in_button.setIconSize(QSize(50, 50))

        font = QFont()
        font.setFamily('monospace')
        # font.setPixelSize(50)
        zoom_in_button.setFont(font)
        zoom_in_button.clicked.connect(self.text_area.zoomIn)

        # zoom out button----------------------------------------
        zoom_out_button = QPushButton()
        zoom_out_button.setFixedSize(50, 40)
        zoom_out_button.setCursor(Qt.CursorShape.PointingHandCursor)
        zoom_out_button.setObjectName("zoom_out_button")
        zoom_out_button.setShortcut("ctrl+down")
        zoom_out_button.setIcon(QIcon(
            self.resources.get_image_path('zoom_out_icon')))
        zoom_out_button.setIconSize(QSize(50, 50))

        font = QFont()
        zoom_out_button.setFont(font)
        zoom_out_button.clicked.connect(self.text_area.zoomOut)

        # theme button-------------------------------------------
        self.theme_button = QPushButton("Change theme")
        self.theme_button.setFixedSize(110, 40)
        self.theme_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.theme_button.setObjectName("theme_button")

        font = QFont()
        font.setFamily('monospace')
        font.setPixelSize(15)
        self.theme_button.setFont(font)
        self.theme_button.clicked.connect(self.toggle_theme)

        self.new_tabb = QTabWidget()

        Layout = QHBoxLayout()
        Layout.addWidget(copy_button)
        Layout.addWidget(cut_button)
        Layout.addWidget(insert_text)
        Layout.addWidget(to_html)
        Layout.addWidget(paste_button)
        Layout.addWidget(undo_button)
        Layout.addWidget(redo_button)
        Layout.addWidget(clear_button)
        Layout.addWidget(zoom_in_button)
        Layout.addWidget(zoom_out_button)
        Layout.addWidget(self.theme_button)

        Layout2 = QVBoxLayout()
        Layout2.addLayout(Layout)
        Layout2.addWidget(self.text_area)
        # Layout2.addWidget(self.new_tabb)

        self.centralWidget.setLayout(Layout2)
        self.setCentralWidget(self.centralWidget)

    def dragEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event: QDropEvent):
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            if urls:
                file_path = urls[0].toLocalFile()  # Get the first file path
                try:
                    with open(file_path, 'r') as file:
                        content = file.read()
                        # Display content in QTextEdit
                        self.text_area.setText(content)
                except Exception as e:
                    self.text_area.setText(f"Failed to read file: {e}")
        else:
            event.ignore()

    def toggle_theme(self):
        if self.current_theme == "light":
            self.current_theme = "dark"
            self.setStyleSheet(self.to_light_theme())
            self.theme_button.setText("Silver Theme")
            self.theme_button.setStyleSheet(
                "background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #7A7979, stop: 1 #2F2D2D); color: #ffffff;")

        elif self.current_theme == "dark":
            self.current_theme = "silver"
            self.setStyleSheet(self.to_silver_gradient_theme())
            self.theme_button.setText("Dark Theme")
            self.theme_button.setStyleSheet(
                "background-color: #000000; color: #ffffff;")

        else:
            self.current_theme = "light"
            self.setStyleSheet(self.to_dark_theme())
            self.theme_button.setText("Light Theme")
            self.theme_button.setStyleSheet(
                "background-color: #ffffff; color: #000000;")

    # Themes--------------------------------------------------------------

    @staticmethod
    def to_light_theme():
        return """
        #Noted{
        background-color: #ffffff;
        }
        
        #text_area{
            background-color: #ffffff;
            color: #000000;
            border-radius: 20px;
        }
        
        #setmenu{
            border-radius: 10px;
            background-color: #a3a3a3;
            color: #000000;
        }
        
        QPushButton#insert_text{
            border-radius: 14px;
            background-color: #362300;
            color: #ffffff;
        }
        QPushButton#insert_text:hover{
            border-radius: 14px;
            background-color: #878787;
            color: #000000;
        }
        
        QPushButton#to_html{
            border-radius: 14px;
            background-color:  #362300;
            color: #ffffff;
        }
        
        QPushButton#to_html:hover{
            border-radius: 14px;
            background-color: #878787;
            color: #000000;
        }
        
        
        QPushButton#copy_button{
            border-radius: 14px;
            background-color: #000000;
            color: #ffffff;
        }
        QPushButton#copy_button:hover{
            background-color: #878787;
            color: #000000;
        }
        QPushButton#cut_button{
            border-radius: 14px;
            background-color: #1c0002;
            color: #ffffff;
        }
        QPushButton#cut_button:hover{
            background-color: #878787;
            color: #000000;
        }
        QPushButton#paste_button{
            border-radius: 14px;
            background-color: #080024;
            color: #ffffff;
        }
        QPushButton#paste_button:hover{
            background-color: #878787;
            color: #000000;
        }
        QPushButton#undo_button{
            border-radius: 14px;
            background-color: #001c04;
            color: #ffffff;
        }
        QPushButton#undo_button:hover{
            background-color: #878787;
            color: #000000;
        }
        QPushButton#redo_button{
            border-radius: 14px;
            background-color: #00191a;
            color: #ffffff;
        }
        QPushButton#redo_button:hover{
            background-color: #878787;
            color: #000000;
        }

        QPushButton#clear_button{
            border-radius: 14px;
            background-color: #0b011a;
            color: #ffffff;
        }
        QPushButton#clear_button:hover{
            background-color: #878787;
            color: #000000;
        }
        
            
        QPushButton#zoom_in_button{
            background-color: #e3e3e3;
            border-radius: 20px;
        }
        QPushButton#zoom_out_button{
            background-color: #e3e3e3;
            border-radius: 20px;
        }
        
        QPushButton#theme_button{
            background-color: #000000;
            border-radius: 14px;
        }
        """

    @staticmethod
    def to_dark_theme():
        return """
        #Noted{
            background-color: #151700;
        }
        
        #text_area{
            background-color: #000000;
            color: #ffffff;
            border-radius: 20px;
        }
        
        #setmenu{
            border-radius: 10px;
            background-color: #000000;
            color: #ffffff;
        }
        
              
        QPushButton#insert_text{
            border-radius: 14px;
            background-color: #362300;
            color: #ffffff;
        }
        
              
        QPushButton#insert_text:hover{
            border-radius: 14px;
            background-color: #000000;
            color: #ffffff;
        }
        
                 
        QPushButton#to_html{
            border-radius: 14px;
            background-color: #a63a00;
            color: #ffffff;
        }
        
        QPushButton#to_html:hover{
            border-radius: 14px;
            background-color: #000000;
            color: #ffffff;
        }
        
        
    
        #copy_button{
            border-radius: 14px;
            background-color: #ffffff;
            color: #000000;
        }
        #copy_button:hover{
            background-color: #000000;
            color: #ffffff;
        }
        #cut_button{
            border-radius: 14px;
            background-color: #1c0002;
            color: #ffffff;
        }
        #cut_button:hover{
            background-color: #000000;
            color: #ffffff;
        }
        #paste_button{
            border-radius: 14px;
            background-color: #080024;
            color: #ffffff;
        }
        #paste_button:hover{
            background-color: #000000;
            color: #ffffff;
        }
        #undo_button{
            border-radius: 14px;
            background-color: #001c04;
            color: #ffffff;
        }
        #undo_button:hover{
            background-color: #000000;
            color: #ffffff;
        }
        #redo_button{
            border-radius: 14px;
            background-color: #00191a;
            color: #ffffff;
        }
        #redo_button:hover{
            background-color: #000000;
            color: #ffffff;
        }

        #clear_button{
            border-radius: 14px;
            background-color: #0b011a;
            color: #ffffff;
        }
        #clear_button:hover{
            background-color: #000000;
            color: #ffffff;
        }
        
        QPushButton#zoom_in_button{
            background-color: #e3e3e3;
            border-radius: 20px;
        }
        QPushButton#zoom_out_button{
            background-color: #e3e3e3;
            border-radius: 20px;
        }
             
        QPushButton#theme_button{
            background-color: #ffffff;
            color: #000000;
            border-radius: 14px;
        }

        """

    @staticmethod
    def to_silver_gradient_theme():
        return """
        #Noted{
            background: qlineargradient(
                x1: 0, y1: 0, x2: 0, y2: 1,
                stop: 0 #888888,
                stop: 1 #232324
            );
        }
        
        #text_area{
            background: qlineargradient(
                x1: 0, y1: 0, x2: 0, y2: 1,
                stop: 0 #060606,
                stop: 1 #313132
            );
            color: #ffffff;
            border-radius: 20px;
        }
        
        #setmenu{
            border-radius: 10px;
            background-color: #010406;
            color: #ffffff;
        }
        
        #copy_button{
            border-radius: 14px;
            background-color: #ffffff;
            color: #000000;
        }
        #copy_button:hover{
            background-color: #272626;
            color: #ffffff;
        }
        #cut_button{
            border-radius: 14px;
            background-color: #1c0002;
            color: #ffffff;
        }
        #cut_button:hover{
            background-color: #272626;
            color: #ffffff;
        }
        QPushButton#insert_text{
            border-radius: 14px;
            background-color: #362300;
            color: #ffffff;
        }
        QPushButton#insert_text:hover{
            border-radius: 14px;
            background-color: #272626;
            color: #ffffff;
        }
        
        QPushButton#to_html{
            border-radius: 14px;
            background-color:  #362300;
            color: #ffffff;
        }
        
        QPushButton#to_html:hover{
            border-radius: 14px;
            background-color: #272626;
            color: #ffffff;
        }
        
        
        QPushButton#paste_button{
            border-radius: 14px;
            background-color: #080024;
            color: #ffffff;
        }
        QPushButton#paste_button:hover{
            background-color: #272626;
            color: #ffffff;
        }
        QPushButton#undo_button{
            border-radius: 14px;
            background-color: #001c04;
            color: #ffffff;
        }
        QPushButton#undo_button:hover{
           background-color: #272626;
            color: #ffffff;
        }
        QPushButton#redo_button{
            border-radius: 14px;
            background-color: #00191a;
            color: #ffffff;
        }
        QPushButton#redo_button:hover{
           background-color: #272626;
           color: #ffffff;
        }

        QPushButton#clear_button{
            border-radius: 14px;
            background-color: #0b011a;
            color: #ffffff;
        }
        QPushButton#clear_button:hover{
            background-color: #272626;
            color: #ffffff;
        }
        
            
        QPushButton#zoom_in_button{
            background-color: #e3e3e3;
            border-radius: 20px;
        }
        QPushButton#zoom_out_button{
            background-color: #e3e3e3;
            border-radius: 20px;
        }
        
        QPushButton#theme_button{
            background-color: #000000;
            border-radius: 14px;
        }
        """

    # --------------------------------------------------------------

    def plain_random_text(self):
        self.text_area.insertPlainText(
            """
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

            Maecenas volutpat blandit aliquam etiam erat velit scelerisque in dictum. Pellentesque elit ullamcorper dignissim cras tincidunt lobortis. Semper quis lectus nulla at volutpat diam ut venenatis. Dui sapien eget mi proin sed libero enim sed faucibus. Tempus egestas sed sed risus pretium quam vulputate dignissim. Ac turpis egestas integer eget aliquet. Eget magna fermentum iaculis eu non. Ut tristique et egestas quis.

            Sed egestas egestas fringilla phasellus faucibus. Nibh venenatis cras sed felis eget velit aliquet sagittis id. Turpis egestas integer eget aliquet. Ac auctor augue mauris augue neque gravida in fermentum et. Amet volutpat consequat mauris nunc congue nisi vitae. Nisl vel pretium lectus quam id leo in vitae turpis. Dignissim cras tincidunt lobortis feugiat vivamus at augue eget arcu. Amet risus nullam eget felis eget nunc. Pretium vulputate sapien nec sagittis aliquam malesuada. Orci dapibus ultrices in iaculis nunc sed augue lacus viverra. Ornare lectus sit amet est placerat in egestas erat imperdiet.

        """
        )

    def to_html_format(self):
        to_html = self.text_area.toHtml()
        self.text_area.setPlainText(to_html)

    def open_file_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Open File", "", "All Files (*);;Text Files (*.txt)"
        )
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    content = file.read()

                self.text_area.setPlainText(content)

            except Exception as e:
                self.error = QMessageBox()
                self.error.critical(
                    self, "Error", f"An error occurred: {str(e)}", QMessageBox.StandardButton.Ok
                )

    def save_file(self):
        open_dialog = QFileDialog(self)
        save = open_dialog.getSaveFileName(
            self, "Save File", "", "All Files (*);;Text Files (*.txt)"
        )
        if save:
            try:
                with open(save[0], 'w') as file:
                    file.write(self.text_area.toPlainText())
            except Exception as e:
                self.error = QMessageBox()
                self.error.critical(
                    self, "Error", f"An error occurred: {str(e)}", QMessageBox.StandardButton.Ok
                )

    def save_as(self):
        file_save = QFileDialog(self)
        save_ = file_save.getSaveFileName(
            self, "Save File", "", "All Files (*);;Text Files (*.txt)"
        )
        if save_:
            try:
                with open(save_[0], 'w') as file:
                    file.write(self.text_area.toPlainText())
            except Exception as e:
                self.error = QMessageBox()
                self.error.critical(
                    self, "Error", f"An error occurred: {str(e)}", QMessageBox.StandardButton.Ok
                )

    def open_calculator(self):
        try:
            if os.name == 'nt':
                os.system("start calc")
            else:
                raise FileNotFoundError(
                    "Windows calculator is not available on this device.")

        except FileNotFoundError:
            self.error = QMessageBox()
            self.error.critical(
                self, "Not found ;-;", "Windows calculator is not available on your system. It seems like your system is not Windows", QMessageBox.StandardButton.Ok)

    def open_ms_word(self):
        try:
            if os.name == 'nt':
                os.system("start winword")
            else:
                raise FileNotFoundError(
                    "MS Word is not available on this device.")
        except FileNotFoundError:
            self.error = QMessageBox()
            self.error.critical(
                self, "Not found ;-;", "MS Word does not found in your system", QMessageBox.StandardButton.Ok)

    def open_ms_excel(self):
        try:

            if os.name == 'nt':
                os.system("start excel")
            else:
                raise FileNotFoundError(
                    "MS Excel is not available on this device.")
        except FileNotFoundError:
            self.error = QMessageBox()
            self.error.critical(
                self, "Not found ;-;", "MS Excel does not found on your system", QMessageBox.StandardButton.Ok
            )

    def open_ms_access(self):
        try:
            if os.name == 'nt':
                os.system("start msaccess")
            else:
                raise FileNotFoundError(
                    "MS Access is not available on this device.")
        except FileNotFoundError:
            self.error = QMessageBox()
            self.error.critical(
                self, "Not found ;-;", "MS Access does not found on your system", QMessageBox.StandardButton.Ok
            )

    def open_ms_powerpoint(self):
        try:
            # Check if it's a Windows system
            if os.name == 'nt':
                # Try opening PowerPoint
                os.system("start powerpnt")
            else:
                # For non-Windows platforms, show an error
                raise FileNotFoundError(
                    "PowerPoint is not available on this device.")

        except FileNotFoundError:
            # Create and show the error message
            self.error = QMessageBox()
            self.error.critical(
                self, "Not found ;-;", "PowerPoint does not found on your system", QMessageBox.StandardButton.Ok)

    def open_ms_outlook(self):
        try:

            if os.name == 'nt':
                os.system("start outlook")
            else:
                raise FileNotFoundError(
                    "Outlook is not available on this device.")

        except FileNotFoundError:
            self.error = QMessageBox()
            self.error.critical(
                self, "Not found ;-;", "Outlook does not found on your system.", QMessageBox.StandardButton.Ok)

    def open_ms_teams(self):
        try:
            if os.name == 'nt':
                os.system("start ms-teams")
            else:
                raise FileNotFoundError(
                    "Teams is not available on this device.")

        except FileNotFoundError:
            self.error = QMessageBox()
            self.error.critical(
                self, "Not found ;-;", "Teams does not found on your system.", QMessageBox.StandardButton.Ok)

    def open_vscode(self):
        try:
            os.system('code')
        except FileNotFoundError:
            self.error = QMessageBox()
            self.error.critical(
                self, "Not found ;-;", "Visual Studio Code does not found on your system.\nPlease install it first by visiting https://code.visualstudio.com/", QMessageBox.StandardButton.Ok)

    def open_vs(self):
        try:
            os.system('start devenv')
        except FileNotFoundError:
            self.error = QMessageBox()
            self.error.critical(
                self, "Not found ;-;", "Visual Studio does not found on your system.\nPlease install it first by visiting https://visualstudio.microsoft.com/", QMessageBox.StandardButton.Ok)

    def open_paint(self):
        try:
            if os.name == 'nt':
                os.system('start mspaint')
            else:
                raise FileNotFoundError(
                    "Paint is not available on this device.")
        except FileNotFoundError:
            self.error = QMessageBox()
            self.error.critical(
                self, "Not found ;-;", "Windows paint does not found on your system. It seems like your system is not Windows", QMessageBox.StandardButton.Ok)

    def open_canva(self):
        try:
            if os.path.exists("C:/Users/1973r/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Canva.lnk"):
                os.startfile(
                    "C:/Users/1973r/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Canva.lnk")
            else:
                raise FileNotFoundError(
                    "Canva is not available on this device.")
        except FileNotFoundError:
            self.error = QMessageBox()
            self.error.critical(
                self, "Not found ;-;", "Canva is not installed on your system\nPlease install it first by given link https://www.canva.com/", QMessageBox.StandardButton.Ok
            )

    def open_win_sec(self):
        try:
            if os.name == 'nt':
                os.system('start windowsdefender:')
            else:
                raise FileNotFoundError(
                    "Windows Defender is not available on this device.")
        except FileNotFoundError:
            self.error = QMessageBox()
            self.error.critical(
                self, "Not found ;-;", "Windows Defender does not found on your system. It seems like your system is not Windows", QMessageBox.StandardButton.Ok)

    def open_task_manager(self):
        try:
            if os.name == 'nt':
                os.system("start taskmgr")
            else:
                raise FileNotFoundError(
                    "Task Manager is not available on this device.")
        except FileNotFoundError:
            self.error = QMessageBox()
            self.error.critical(
                self, "Not found ;-;", "Task Manager does not found on your system. It seems like your system is not Windows", QMessageBox.StandardButton.Ok)

    def open_snipping_tool(self):
        try:
            if os.name == 'nt':
                os.system('start snippingtool')
            else:
                raise FileNotFoundError(
                    "Snipping Tool is not available on this device.")
        except FileNotFoundError:
            self.error = QMessageBox()
            self.error.critical(
                self, "Not found ;-;", "Windows snipping tool does not found on your system. It seems like your system is not Windows", QMessageBox.StandardButton.Ok)

    def open_Resource_monitor(self):
        try:
            if os.name == 'nt':
                os.system('start resmon')
            else:
                raise FileNotFoundError(

                    "Resource Monitor is not available on this device.")
        except FileNotFoundError:
            self.error = QMessageBox()
            self.error.critical(
                self, "Not found ;-;", "Windows resource monitor does not found on your system. It seems like your system is not Windows", QMessageBox.StandardButton.Ok
            )

    def open_performance_monitor(self):
        try:
            if os.name == 'nt':
                os.system('start perfmon')
            else:
                raise FileNotFoundError(
                    "Performance Monitor is not available on this device.")
        except FileNotFoundError:
            self.error = QMessageBox()
            self.error.critical(
                self, "Not found ;-;", "Windows performance monitor does not found on your system. It seems like your system is not Windows", QMessageBox.StandardButton.Ok
            )

    def open_wordpad(self):
        try:
            if os.name == 'nt':
                os.system("start write")
            else:
                raise FileNotFoundError(
                    "Wordpad is not available on this device.")
        except FileNotFoundError:
            self.error = QMessageBox()
            self.error.critical(
                self, "Not found ;-;", "Wordpad does not found on your system", QMessageBox.StandardButton.Ok)

    def open_registery_editor(self):
        try:
            if os.name == 'nt':
                os.system("regedit")
            else:
                raise FileNotFoundError(
                    "Registry Editor is not available on this device.")
        except FileNotFoundError:
            self.error = QMessageBox()
            self.error.critical(
                self, "Nor found ;-;", "Registry Editor does not found on your system", QMessageBox.StandardButton.Ok)

    def open_settings(self):
        try:
            if os.name == 'nt':
                os.system('start ms-settings:')
            else:
                raise FileNotFoundError(
                    "Windows settings is not available on this device.")
        except FileNotFoundError:
            self.error = QMessageBox()
            self.error.critical(
                self, "Not found ;-;", "Windows settings does not found on your system. It seems like your system is not Windows", QMessageBox.StandardButton.Ok)

    def open_clock(self):
        try:
            if os.name == 'nt':
                os.system("start ms-clock:")
            else:
                raise FileNotFoundError(
                    "Clock is not available on this device.")
        except FileNotFoundError:
            self.error = QMessageBox()
            self.error.critical(
                self, "Not found ;-;", "Windows clock is not found on your device. It seems like your system is not Windows", QMessageBox.StandardButton.Ok)

    def open_terminal(self):
        try:
            if os.name == 'nt':
                os.system('start cmd')
            else:
                raise FileNotFoundError(
                    "Windows terminal is not available on this device.")
        except FileNotFoundError:
            self.error = QMessageBox()
            self.error.critical(
                self, "Not found ;-;", "Wndows terminal is not found on your device. It seems like your system is not Windows", QMessageBox.StandardButton.Ok)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    splash_pix = QPixmap(resource_path("Noted_s_banner.png")).scaled(
        1000, 1000, Qt.AspectRatioMode.KeepAspectRatio)
    splash = QSplashScreen(splash_pix, Qt.WindowType.WindowStaysOnTopHint)
    splash.show()

    QTimer.singleShot(2000, splash.close)
    QTimer.singleShot(2000, lambda: window.show())

    window = mainwin()
    sys.exit(app.exec())
