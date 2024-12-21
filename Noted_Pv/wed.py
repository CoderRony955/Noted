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
    QToolBar,
    QTabWidget,
    QSplashScreen,
    QFileDialog,

)
from PyQt6.QtGui import QIcon, QFont, QCursor, QDragEnterEvent, QDropEvent, QPixmap
from PyQt6.QtCore import Qt, QSize, QTimer
from themes import themes
import os
import webbrowser
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
    abs_path = os.path.join(base_path, 'icons_pv', relative_path)
    print(f"Resolved path for {relative_path}: {abs_path}")  # Debugging
    return abs_path


class ResourceManager:
    def __init__(self):
        # Use relative paths to image files
        self.images = {
            "Noted_platinum": resource_path("Noted_P.png"),
            "blue_sky_icon": resource_path("Blue_sky_icon.png"),
            "brave_icon": resource_path("brave_browser_icon.png"),
            "chatgpt_icon": resource_path("Chatgpt_icon.png"),
            "chrome_icon": resource_path("Chrome_icon.png"),
            'gmail_icon': resource_path("gmail_icon.png"),
            "claude_ai_icon": resource_path("claude_ai_icon.png"),
            "edge_icon": resource_path("Edge_icon.png"),
            "facebook_icon": resource_path("Facebook_icon.png"),
            "gemini_icon": resource_path("Gemini_icon.png"),
            "github_icon": resource_path("Github_icon.png"),
            "google_icon": resource_path("Google_icon.png"),
            "instagram_icon": resource_path("Instagram_icon.png"),
            "linkedin_icon": resource_path("Linkedin_icon.png"),
            "opera_icon": resource_path("Opera_icon.png"),
            "spotify_icon": resource_path("Spotify_icon.png"),
            "twitter_icon": resource_path("X_icon.png"),
            "threads_icon": resource_path("Threads_icon.png"),
            "youtube_icon": resource_path("Yt_icon.png"),
            "discord_icon": resource_path("discord_icon.png"),
            "reddit_icon": resource_path("reddit_icon.png"),
            "zoom_in_icon": resource_path("zoom_in_magnifier.png"),
            "zoom_out_icon": resource_path("zoom_out_magnifier.png"),

        }

    def get_image_path(self, name):
        """ Retrieve the path of an image by its key """
        return self.images.get(name, None)


class mainwin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.centralWidget = QWidget()
        self.resources = ResourceManager()
        self.setWindowTitle("Noted Platinum")
        self.setGeometry(300, 300, 1000, 650)
        self.setWindowIcon(
            QIcon(self.resources.get_image_path("Noted_platinum")))

        self.setObjectName("Noted")

        self.current_theme = 'dark'
        self.setStyleSheet(self.to_dark_theme())

        splash.show()
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

        MT = setmenu.addMenu('More themes')

        Binary = MT.addAction('Binary')
        Binary.setShortcut('ctrl+alt+b')
        Binary.triggered.connect(self.apply_binary_theme)

        Dark_ocean = MT.addAction('Dark ocean')
        Dark_ocean.setShortcut('ctrl+shift+d')
        Dark_ocean.triggered.connect(self.apply_dark_ocean_theme)

        Diamond_gradient = MT.addAction('Diamond')
        Diamond_gradient.setShortcut('alt+d')
        Diamond_gradient.triggered.connect(self.apply_diamond_gradient_theme)

        Dracula_gradient = MT.addAction('Dracula')
        Dracula_gradient.setShortcut('ctrl+alt+d')
        Dracula_gradient.triggered.connect(self.apply_dracula_gradient_theme)

        Cute_purple = MT.addAction('Cute purple')
        Cute_purple.setShortcut('shift+p')
        Cute_purple.triggered.connect(self.apply_cute_purple_theme)

        Rose = MT.addAction('Rose')
        Rose.setShortcut('ctrl+alt+r')
        Rose.triggered.connect(self.apply_rose_theme)

        Noted_platinum = MT.addAction('Noted platinum')
        Noted_platinum.setShortcut('ctrl+alt+n')
        Noted_platinum.triggered.connect(self.apply_noted_platinum_theme)

        Grass = MT.addAction('Grass')
        Grass.setShortcut('ctrl+alt+g')
        Grass.triggered.connect(self.apply_grass_theme)

        Silver = MT.addAction('Silver')
        Silver.setShortcut('ctrl+alt+l')
        Silver.triggered.connect(self.apply_silver_theme)

        Star_wars = MT.addAction('Star wars')
        Star_wars.setShortcut('ctrl+shift+a')
        Star_wars.triggered.connect(self.apply_star_wars_theme)

        Sunny_gradient = MT.addAction('Sunny')
        Sunny_gradient.setShortcut('alt+s')
        Sunny_gradient.triggered.connect(self.apply_sunny_gradient_theme)

        Gamer_gradient = MT.addAction('Gamer')
        Gamer_gradient.setShortcut('alt+g')
        Gamer_gradient.triggered.connect(self.apply_gamer_gradient_theme)

        Programmer = MT.addAction('Programmer')
        Programmer.setShortcut('shift+alt+p')
        Programmer.triggered.connect(self.apply_programmer_theme)

        Honey_bee = MT.addAction('Honey bee')
        Honey_bee.setShortcut('ctrl+alt+h')
        Honey_bee.triggered.connect(self.apply_honey_bee_theme)

        Milky_way = MT.addAction('Milky way')
        Milky_way.setShortcut('ctrl+alt+m')
        Milky_way.triggered.connect(self.apply_milky_way_theme)

        Volanic = MT.addAction('Volcanic')
        Volanic.setShortcut('ctrl+alt+v')
        Volanic.triggered.connect(self.apply_volanic_theme)

        Fonts = setmenu.addMenu("Fonts")

        Algerian = Fonts.addAction('Algerian')
        Algerian.triggered.connect(self.Algerian)

        Arial = Fonts.addAction('Arial')
        Arial.triggered.connect(self.Arial)

        Bahnschrift = Fonts.addAction('Bahnschrift')
        Bahnschrift.triggered.connect(self.Bahnschrift)

        Century = Fonts.addAction('Century')
        Century.triggered.connect(self.Century)

        Corbel = Fonts.addAction('Corbel')
        Corbel.triggered.connect(self.Corbel)

        Calibri = Fonts.addAction('Calibri')
        Calibri.triggered.connect(self.Calibri)

        Elephant = Fonts.addAction('Elephant')
        Elephant.triggered.connect(self.Elephant)

        Ebrima = Fonts.addAction('Ebrima')
        Ebrima.triggered.connect(self.Ebrima)

        Forte = Fonts.addAction('Forte')
        Forte.triggered.connect(self.Forte)

        Georgia = Fonts.addAction('Georgia')
        Georgia.triggered.connect(self.Georgia)

        Harrington = Fonts.addAction('Harrington')
        Harrington.triggered.connect(self.Harrington)

        System = Fonts.addAction('System')
        System.triggered.connect(self.System)

        Terminal = Fonts.addAction('Terminal')
        Terminal.triggered.connect(self.Terminal)

        Impact = Fonts.addAction('Impact')
        Impact.triggered.connect(self.Impact)

        Ink_Free = Fonts.addAction('Ink Free')
        Ink_Free.triggered.connect(self.Ink_Free)

        Jokerman = Fonts.addAction('Jokerman')
        Jokerman.triggered.connect(self.Jokerman)

        monospace = Fonts.addAction("Monospace")
        monospace.triggered.connect(self.monospace)

        Verdana = Fonts.addAction('Verdana')
        Verdana.triggered.connect(self.verdana)

        Wingdings = Fonts.addAction('Wingdings')
        Wingdings.triggered.connect(self.Wingdings)

        # More actions -------------------------------------------
        more_actions = QToolBar()
        more_actions.setMovable(True)
        self.addToolBar(more_actions)

        # Google open shortcut
        open_google = more_actions.addAction('Open Google')
        open_google.setIcon(
            QIcon(self.resources.get_image_path("google_icon")))
        open_google.setToolTip('Open Google')
        open_google.triggered.connect(
            lambda: webbrowser.open('http://www.google.com'))

        # Edge browser shortcut
        open_edge = more_actions.addAction('Open Edge')
        open_edge.setIcon(
            QIcon(self.resources.get_image_path("edge_icon")))
        open_edge.setToolTip('Open Edge')
        open_edge.triggered.connect(self.Open_Edge)

        # Github open shortcut
        open_github = more_actions.addAction('Open Github')
        open_github.setIcon(
            QIcon(self.resources.get_image_path('github_icon')))
        open_github.setToolTip('Open Github')
        open_github.triggered.connect(
            lambda: webbrowser.open('https://github.com/'))

        # gmail open shortcut
        open_gmail = more_actions.addAction('Open Gmail')
        open_gmail.setIcon(
            QIcon(self.resources.get_image_path('gmail_icon')))
        open_gmail.setToolTip('Open Gmail')
        open_gmail.triggered.connect(
            lambda: webbrowser.open('https://mail.google.com'))

        # Youtube open shortcut
        open_yt = more_actions.addAction('Open Youtube')
        open_yt.setIcon(
            QIcon(self.resources.get_image_path('youtube_icon')))
        open_yt.setToolTip('Open Youtube')
        open_yt.triggered.connect(
            lambda: webbrowser.open('https://www.youtube.com/'))

        # Google chrome open shortcut
        open_chrome = more_actions.addAction('Open Chrome')
        open_chrome.setIcon(
            QIcon(self.resources.get_image_path('chrome_icon')))
        open_chrome.setToolTip('Open Chrome')
        open_chrome.triggered.connect(self.Open_Chrome)

        # Opera browser open shortcut
        open_opera = more_actions.addAction('Open Opera')
        open_opera.setIcon(
            QIcon(self.resources.get_image_path('opera_icon')))
        open_opera.setToolTip('Open Opera')
        open_opera.triggered.connect(self.Open_Opera)

        # Spotify open shortcut
        open_spotify = more_actions.addAction('Open Spotify')
        open_spotify.setIcon(
            QIcon(self.resources.get_image_path('spotify_icon')))
        open_spotify.setToolTip('Open Spotify')
        open_spotify.triggered.connect(self.Open_Spotify)

        # Chatgpt open shortcut
        open_chatgpt = more_actions.addAction('Open Chatgpt')
        open_chatgpt.setIcon(
            QIcon(self.resources.get_image_path('chatgpt_icon')))
        open_chatgpt.setToolTip('Open Chatgpt')
        open_chatgpt.triggered.connect(
            lambda: webbrowser.open('https://chat.openai.com/chat'))

        # twitter (x) open shortcut
        open_twitter = more_actions.addAction('Open Twitter')
        open_twitter.setIcon(
            QIcon(self.resources.get_image_path('twitter_icon')))
        open_twitter.setToolTip('Open Twitter')
        open_twitter.triggered.connect(
            lambda: webbrowser.open('https://twitter.com/'))

        # Instagram open shortcut

        open_insta = more_actions.addAction('Open Instagram')
        open_insta.setIcon(
            QIcon(self.resources.get_image_path('instagram_icon')))
        open_insta.setToolTip('Open Instagram')
        open_insta.triggered.connect(
            lambda: webbrowser.open('https://www.instagram.com/'))

        # Threads open shortcut
        open_threads = more_actions.addAction('Open Threads')
        open_threads.setIcon(
            QIcon(self.resources.get_image_path('threads_icon')))
        open_threads.setToolTip('Open Threads')
        open_threads.triggered.connect(
            lambda: webbrowser.open('https://www.threads.net/'))

        # Facbook open shortcut
        open_facebook = more_actions.addAction('Open Facebook')
        open_facebook.setIcon(
            QIcon(self.resources.get_image_path('facebook_icon')))
        open_facebook.setToolTip('Open Facebook')
        open_facebook.triggered.connect(
            lambda: webbrowser.open('https://www.facebook.com/'))

        # Google gemini open shortcut
        open_gemini = more_actions.addAction('Open Gemini')
        open_gemini.setIcon(
            QIcon(self.resources.get_image_path('gemini_icon')))
        open_gemini.setToolTip('Open Google Gemini')
        open_gemini.triggered.connect(
            lambda: webbrowser.open('https://gemini.google.com/'))

        # Claude Ai open shortcut
        open_claude = more_actions.addAction('Open Claude')
        open_claude.setIcon(QIcon(
            self.resources.get_image_path('claude_ai_icon')))
        open_claude.setToolTip('Open Claude')
        open_claude.triggered.connect(
            lambda: webbrowser.open('https://www.claude.ai/'))

        # brave browser open shortcut
        open_brave = more_actions.addAction('Open Brave')
        open_brave.setIcon(QIcon(
            self.resources.get_image_path('brave_icon')))
        open_brave.setToolTip('Open Brave')
        open_brave.triggered.connect(self.Open_Brave)

        # Bluesky open shortcut
        open_bluesky = more_actions.addAction('Open Bluesky')
        open_bluesky.setIcon(
            QIcon(self.resources.get_image_path('blue_sky_icon')))
        open_bluesky.setToolTip('Open bluesky')
        open_bluesky.triggered.connect(
            lambda: webbrowser.open('https://bsky.app/'))

        # Linkdin open shortcut
        open_linkedin = more_actions.addAction('Open Linkedin')
        open_linkedin.setIcon(
            QIcon(self.resources.get_image_path('linkedin_icon')))
        open_linkedin.setToolTip('Open Linkedin')
        open_linkedin.triggered.connect(
            lambda: webbrowser.open('https://www.linkedin.com/'))

        # discord open shortcut
        open_discord = more_actions.addAction('Open Discord')
        open_discord.setIcon(
            QIcon(self.resources.get_image_path('discord_icon')))
        open_discord.setToolTip('Open Discord')
        open_discord.triggered.connect(
            lambda: webbrowser.open('https://discord.com/app/'))

        # reddit open shortcut
        open_reddit = more_actions.addAction('Open Reddit')
        open_reddit.setIcon(
            QIcon(self.resources.get_image_path('reddit_icon')))
        open_reddit.setToolTip('Open Reddit')
        open_reddit.triggered.connect(
            lambda: webbrowser.open('https://www.reddit.com/'))

        # main-----------------------------------------------------------------------

        self.text_area = QTextEdit()
        self.text_area.setObjectName("text_area")
        self.text_area.setPlaceholderText("start writing...")
        self.text_area.setAcceptDrops(True)
        self.text_area.dragEnterEvent = self.dragEnterEvent
        self.text_area.dropEvent = self.dropEvent

        # buttons
        copy_button = QPushButton("Copy")
        copy_button.setFixedSize(110, 40)
        copy_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        copy_button.setObjectName("copy_button")

        font = QFont()
        font.setFamily('monospace')
        font.setPixelSize(15)
        copy_button.setFont(font)
        copy_button.clicked.connect(self.text_area.copy)

        # cutbutton----------------------------------------
        cut_button = QPushButton("Cut")
        cut_button.setFixedSize(110, 40)
        cut_button.setObjectName("cut_button")
        cut_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        font = QFont()
        font.setFamily('monospace')
        font.setPixelSize(15)
        cut_button.setFont(font)
        cut_button.clicked.connect(self.text_area.cut)

        # pastebutton-------------------------------------
        paste_button = QPushButton("Paste")
        paste_button.setFixedSize(110, 40)
        paste_button.setObjectName("paste_button")
        paste_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        font = QFont()
        font.setFamily('monospace')
        font.setPixelSize(15)
        paste_button.setFont(font)
        paste_button.clicked.connect(self.text_area.paste)

        # insert plain text button-------------------------------------
        insert_text = QPushButton("Random text")
        insert_text.setFixedSize(110, 40)
        insert_text.setObjectName("insert_text")
        insert_text.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        font = QFont()
        font.setFamily('monospace')
        font.setPixelSize(13)
        insert_text.setFont(font)
        insert_text.clicked.connect(self.plain_random_text)

        # to html button-------------------------------------
        to_html = QPushButton("To HTML")
        to_html.setFixedSize(110, 40)
        to_html.setShortcut("alt+h")
        to_html.setObjectName("to_html")
        to_html.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        font = QFont()
        font.setFamily('monospace')
        font.setPixelSize(15)
        to_html.setFont(font)
        to_html.clicked.connect(self.to_html_format)

        # undobutton-------------------------------------------
        undo_button = QPushButton("Undo")
        undo_button.setFixedSize(110, 40)
        undo_button.setObjectName("undo_button")
        undo_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        font = QFont()
        font.setFamily('monospace')
        font.setPixelSize(15)
        undo_button.setFont(font)
        undo_button.clicked.connect(self.text_area.undo)

        # redobutton------------------------------------------
        redo_button = QPushButton("Redo")
        redo_button.setFixedSize(110, 40)
        redo_button.setObjectName("redo_button")
        redo_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        font = QFont()
        font.setFamily('monospace')
        font.setPixelSize(15)
        redo_button.setFont(font)
        redo_button.clicked.connect(self.text_area.redo)

        # clearbutton--------------------------------------
        clear_button = QPushButton("Clear")
        clear_button.setFixedSize(110, 40)
        clear_button.setObjectName("clear_button")
        clear_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        font = QFont()
        font.setFamily('monospace')
        font.setPixelSize(15)
        clear_button.setFont(font)
        clear_button.clicked.connect(self.text_area.clear)

        # zoom in button----------------------------------------
        zoom_in_button = QPushButton()
        zoom_in_button.setFixedSize(50, 40)
        zoom_in_button.setObjectName("zoom_in_button")
        zoom_in_button.setShortcut("ctrl+up")
        # zoom_in_button.setIcon(QIcon("icons/zoom_in_magnifier.png"))
        zoom_in_button.setIcon(
            QIcon(self.resources.get_image_path("zoom_in_icon")))
        zoom_in_button.setIconSize(QSize(50, 50))
        zoom_in_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        font = QFont()
        font.setFamily('monospace')
        # font.setPixelSize(50)
        zoom_in_button.setFont(font)
        zoom_in_button.clicked.connect(self.text_area.zoomIn)

        # zoom out button----------------------------------------
        zoom_out_button = QPushButton()
        zoom_out_button.setFixedSize(50, 40)
        zoom_out_button.setObjectName("zoom_out_button")
        zoom_out_button.setShortcut("ctrl+down")
        # zoom_out_button.setIcon(QIcon("icons/zoom_out_magnifier.png"))
        zoom_out_button.setIcon(
            QIcon(self.resources.get_image_path("zoom_out_icon")))
        zoom_out_button.setIconSize(QSize(50, 50))
        zoom_out_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        zoom_out_button.clicked.connect(self.text_area.zoomOut)

        # theme button-------------------------------------------
        self.theme_button = QPushButton("Change theme")
        self.theme_button.setFixedSize(110, 40)
        self.theme_button.setObjectName("theme_button")
        self.theme_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

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

        self.centralWidget.setLayout(Layout2)
        self.setCentralWidget(self.centralWidget)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.accept()  # Accept the drag event
        else:
            event.ignore()  # Ignore if it doesn't contain URLs

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
                    self.error = QMessageBox()
                    self.error.critical(
                        self, "Error", f"Failed to open file: {str(e)}")

        else:
            event.ignore()

    def toggle_theme(self):
        if self.current_theme == "light":
            self.current_theme = "dark"
            self.setStyleSheet(self.to_light_theme())
            self.theme_button.setText("Dark Theme")
            self.theme_button.setStyleSheet(
                "background-color: #000000; color: #ffffff;")
        else:
            self.current_theme = "light"
            self.setStyleSheet(self.to_dark_theme())
            self.theme_button.setText("Light Theme")
            self.theme_button.setStyleSheet(
                "background-color: #ffffff; color: #000000;")

    # Themes ----------------------------------------------------------------

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
            background-color: #1c1c1b;
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

    def apply_binary_theme(self):
        self.setStyleSheet(themes.binary_theme())

    def apply_dark_ocean_theme(self):
        self.setStyleSheet(themes.to_dark_ocean())

    def apply_cute_purple_theme(self):
        self.setStyleSheet(themes.cute_purple_theme())

    def apply_honey_bee_theme(self):
        self.setStyleSheet(themes.honey_bee_theme())

    def apply_milky_way_theme(self):
        self.setStyleSheet(themes.milky_way_theme())

    def apply_volanic_theme(self):
        self.setStyleSheet(themes.volcanic_theme())

    def apply_rose_theme(self):
        self.setStyleSheet(themes.rose_theme())

    def apply_star_wars_theme(self):
        self.setStyleSheet(themes.star_wars_theme())

    def apply_noted_platinum_theme(self):
        self.setStyleSheet(themes.noted_platinum_theme())

    def apply_grass_theme(self):
        self.setStyleSheet(themes.grass_theme())

    def apply_silver_theme(self):
        self.setStyleSheet(themes.silver_theme())

    def apply_dracula_gradient_theme(self):
        self.setStyleSheet(themes.dracula_gradient_theme())

    def apply_sunny_gradient_theme(self):
        self.setStyleSheet(themes.sunny_gradient_theme())

    def apply_gamer_gradient_theme(self):
        self.setStyleSheet(themes.gamer_gradient_theme())

    def apply_diamond_gradient_theme(self):
        self.setStyleSheet(themes.diamond_gradient_theme())

    def apply_programmer_theme(self):
        self.setStyleSheet(themes.programmer_theme())

    # -------------------------------------------------------------------------------
    # Fonts--------------------------------------------------------------------------

    def monospace(self):
        self.text_area.setFont(QFont('Monospace'))

    def verdana(self):
        self.text_area.setFont(QFont('Verdana'))

    def Algerian(self):
        self.text_area.setFont(QFont('Algerian'))

    def Bahnschrift(self):
        self.text_area.setFont(QFont('Bahnschrift'))

    def Arial(self):
        self.text_area.setFont(QFont('Arial'))

    def Century(self):
        self.text_area.setFont(QFont('Century'))

    def Corbel(self):
        self.text_area.setFont(QFont('Corbel'))

    def Calibri(self):
        self.text_area.setFont(QFont('Calibri'))

    def Elephant(self):
        self.text_area.setFont(QFont('Elephant'))

    def Forte(self):
        self.text_area.setFont(QFont('Forte'))

    def Ebrima(self):
        self.text_area.setFont(QFont('Ebrima'))

    def Georgia(self):
        self.text_area.setFont(QFont('Georgia'))

    def Harrington(self):
        self.text_area.setFont(QFont('Harrington'))

    def System(self):
        self.text_area.setFont(QFont('System'))

    def Terminal(self):
        self.text_area.setFont(QFont('Terminal'))

    def Impact(self):
        self.text_area.setFont(QFont('Impact'))

    def Ink_Free(self):
        self.text_area.setFont(QFont('Ink Free'))

    def Jokerman(self):
        self.text_area.setFont(QFont('Jokerman'))

    def Wingdings(self):
        self.text_area.setFont(QFont('Wingdings'))
    # --------------------------------------------------------------------------------------

    def plain_random_text(self):
        self.text_area.insertPlainText(
            """
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

            Maecenas volutpat blandit aliquam etiam erat velit scelerisque in dictum. Pellentesque elit ullamcorper dignissim cras tincidunt lobortis. Semper quis lectus nulla at volutpat diam ut venenatis. Dui sapien eget mi proin sed libero enim sed faucibus. Tempus egestas sed sed risus pretium quam vulputate dignissim. Ac turpis egestas integer eget aliquet. Eget magna fermentum iaculis eu non. Ut tristique et egestas quis.

            Sed egestas egestas fringilla phasellus faucibus. Nibh venenatis cras sed felis eget velit aliquet sagittis id. Turpis egestas integer eget aliquet. Ac auctor augue mauris augue neque gravida in fermentum et. Amet volutpat consequat mauris nunc congue nisi vitae. Nisl vel pretium lectus quam id leo in vitae turpis. Dignissim cras tincidunt lobortis feugiat vivamus at augue eget arcu. Amet risus nullam eget felis eget nunc. Pretium vulputate sapien nec sagittis aliquam malesuada. Orci dapibus ultrices in iaculis nunc sed augue lacus viverra. Ornare lectus sit amet est placerat in egestas erat imperdiet.

        """
        )

    def Open_Edge(self):
        try:
            if os.name == 'nt':
                os.system("start msedge")
            else:
                raise FileNotFoundError(
                    "Edge is not available on this device.")
        except FileNotFoundError:
            self.error = QMessageBox()
            self.error.critical(
                self, "Not found ;-;", "Can't open edge", QMessageBox.StandardButton.Ok
            )

    def Open_Opera(self):
        try:
            os.system("start opera")
        except FileNotFoundError:
            self.error = QMessageBox()
            self.error.critical(
                self, "Not found ;-;", "Can't open opera", QMessageBox.StandardButton.Ok
            )

    def Open_Chrome(self):
        try:
            os.system("start chrome")
        except FileNotFoundError:
            self.error = QMessageBox()
            self.error.critical(
                self, "Not found ;-;", "Can't open google chrome", QMessageBox.StandardButton.Ok)

    def Open_Spotify(self):
        try:
            os.system("start spotify")
        except FileNotFoundError:
            self.error = QMessageBox()
            self.error.critical(
                self, "Not found ;-;", "Can't open spotify", QMessageBox.StandardButton.Ok)

    def Open_Brave(self):
        try:
            os.system("start brave")
        except FileNotFoundError:
            self.error = QMessageBox()
            self.error.critical(
                self, "Not found ;-;", "Can't open brave", QMessageBox.StandardButton.Ok
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
                print(e)

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
                print(e)

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
                self, "Not found ;-;", "Visual Studio Code is not installed on this system\nPlease install it first by given link https://code.visualstudio.com/", QMessageBox.StandardButton.Ok
            )

    def open_vs(self):
        try:
            os.system('start devenv')

        except FileNotFoundError:
            self.error = QMessageBox()
            self.error.critical(
                self, "Not found ;-;", "Visual Studio is not installed on this system\nPlease install it first by visiting https://visualstudio.microsoft.com/", QMessageBox.StandardButton.Ok
            )
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
    # with open('Noted main\Styling.qss', 'r') as f:
    #     app.setStyleSheet(f.read())
    # Replace with your splash image file
    splash_pix = QPixmap(resource_path("Noted_p_banner.png")).scaled(
        1000, 1000, Qt.AspectRatioMode.KeepAspectRatio
    )
    splash = QSplashScreen(splash_pix, Qt.WindowType.WindowStaysOnTopHint)
    splash.show()

    window = mainwin()
    QTimer.singleShot(2000, splash.close)
    QTimer.singleShot(2000, lambda: window.show())

    sys.exit(app.exec())
