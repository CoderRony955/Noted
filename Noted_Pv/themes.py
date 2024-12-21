from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QTabWidget
from PyQt6.QtGui import QFont


class themes:

    @staticmethod
    def binary_theme():
        return """
         #Noted{
            background: qlineargradient(
                x1: 0, y1: 0, x2: 0, y2: 1,
                stop: 0 #222220,
                stop: 0.5 #194502,
                stop: 1 #58B402
               
            );
        }
        
        #text_area{
            background: qlineargradient(
                x1: 0, y1: 0, x2: 0, y2: 1,
                stop: 0 #181718,
                stop: 1 #0F0623
            );
            color: #ffffff;
            border-radius: 20px;
        }
        
        #setmenu{
            border-radius: 10px;
            background-color: #0A1703;
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

    @staticmethod
    def to_dark_ocean():
        return """
        #Noted{
            background-color: #040026;
        }
        
        #text_area{
            background-color: #040026;
            color: #ffffff;
            border-radius: 20px;
        }
        
        #setmenu{
            border-radius: 10px;
            background-color: #00005c;
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
    def cute_purple_theme():
        return """
        #Noted{
            background-color: #7800cf;
        }
        
        #text_area{
            background-color: #7800cf;
            color: #000000;
            border-radius: 20px;
           
        }
        
        #setmenu{
            border-radius: 10px;
            background-color: #c194e0;
            color: #000000;
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
    def honey_bee_theme():
        return """
        #Noted{
            background-color: #e0bc04;
        }
        
        #text_area{
            background-color: #e0bc04;
            color: #000000;
            border-radius: 20px;
        }
        
        #setmenu{
            border-radius: 10px;
            background-color: #0f011a;
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
    def milky_way_theme():
        return """
            #Noted{
            background-color: #130026;
        }
        
        #text_area{
            background-color: #130026;
            color: #ffffff;
            border-radius: 20px;
        }
        
        #setmenu{
            border-radius: 10px;
            background-color: #08000f;
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
    def volcanic_theme():
        return """
        #Noted{
            background-color: #bd3b04;
        }
        
        #text_area{
            background-color: #521800;
            color: #ffffff;
            border-radius: 20px;
        }
        
        #setmenu{
            border-radius: 10px;
            background-color: #783501;
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
    def rose_theme():
        return """
        #Noted{
            background-color: #ff0008;
        }
        
        #text_area{
            background-color: #691828;
            color: #ffffff;
            border-radius: 20px;
        }
        
        #setmenu{
            border-radius: 10px;
            background-color: #5e0000;
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
    def noted_platinum_theme():
        return """
          #Noted{
            background-color: #5100ff;
        }
        
        #text_area{
            background-color: #130029;
            color: #ffffff;
            border-radius: 20px;
        }
        
        #setmenu{
            border-radius: 10px;
            background-color: #d4abff;
            color: #000000;
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
    def grass_theme():
        return """
          #Noted{
            background-color: #b1ff0a;
        }
        
        #text_area{
            background-color: #074707;
            color: #ffffff;
            border-radius: 20px;
        }
        
        #setmenu{
            border-radius: 10px;
            background-color: #345c00;
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
    def silver_theme():
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

    @staticmethod
    def dracula_gradient_theme():

        return """
        #Noted{
            background: qlineargradient(
                x1: 0, y1: 0, x2: 0, y2: 1,
                stop: 0 #6a00ff,
                stop: 0.5 #4c00ff,
                stop: 1 #6200ff
            );
        }
        
        #text_area{
            background: qlineargradient(
                x1: 0, y1: 0, x2: 0, y2: 1,
                stop: 0 #EE4BFD,
    
                stop: 1 #7A03E9
            );
            color: #000000;
            border-radius: 20px;
        }
        
        #setmenu{
            border-radius: 10px;
            background-color: #3d0073;
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
    def sunny_gradient_theme():
        return """
        #Noted{
            background-color: #ffc170;
        }
        
        #text_area{
            background: qlineargradient(
                x1: 0, y1: 0, x2: 0, y2: 1,
                stop: 0 #CE8106,
            
                stop: 1 #ccc902
            );
            color: #000000;
            border-radius: 20px;
        }
        
        #setmenu{
            border-radius: 10px;
            background-color: #ffdd19;
            color: #000000;
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
    def gamer_gradient_theme():
        return """
        #Noted{
             background: qlineargradient(
                x1: 0, y1: 0, x2: 0, y2: 1,
                stop: 0 #ff545d,
                stop: 1 #1900ff
            );
        }
        
        #text_area{
            background: qlineargradient(
                x1: 0, y1: 0, x2: 0, y2: 1,
                stop: 0 #04011a,
                stop: 1 #260202
            );
            color: #ffffff;
            border-radius: 20px;
        }
        
        #setmenu{
            border-radius: 10px;
            background-color: #1f1936;
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
    def diamond_gradient_theme():
        return """
        #Noted{
             background: qlineargradient(
                x1: 0, y1: 0, x2: 0, y2: 1,
                stop: 0 #01084D,
                stop: 0.5 #019AF8,
                stop: 1 #A8E7FE
            );
        }
        
        #text_area{
            background: qlineargradient(
                x1: 0, y1: 0, x2: 0, y2: 1,
                stop: 0 #390240,
                stop: 1 #02012C
            );
            color: #ffffff;
            border-radius: 20px;
        }
        
        #setmenu{
            border-radius: 10px;
            background-color: #1B1028;
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
    def programmer_theme():
        return """
     #Noted{
            background: qlineargradient(
                x1: 0, y1: 0, x2: 0, y2: 1,
                stop: 0 #060270,
                stop: 0.5 #E4080A,
                stop: 1 #E8E00A
               
            );
        }
        
        #text_area{
            background: qlineargradient(
                x1: 0, y1: 0, x2: 0, y2: 1,
                stop: 0 #034536,
                stop: 1 #050335
            );
            color: #ffffff;
            border-radius: 20px;
        }
        
        #setmenu{
            border-radius: 10px;
            background-color: #1C022D;
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

    @staticmethod
    def star_wars_theme():
        return """
         #Noted{
            background: qlineargradient(
                x1: 0, y1: 0, x2: 0, y2: 1,
                stop: 0 #1C1D1C,
                stop: 0.5 #03023E,
                stop: 1 #BD8F25
               
            );
        }
        
        #text_area{
            background: qlineargradient(
                x1: 0, y1: 0, x2: 0, y2: 1,
                stop: 0 #500000,
                stop: 1 #1D251E
            );
            color: #ffffff;
            border-radius: 20px;
        }
        
        #setmenu{
            border-radius: 10px;
            background-color: #33092C;
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
