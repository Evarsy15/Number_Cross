import os
from PySide6.QtCore import Qt, QObject, QRect, QRectF, Signal, Slot
from PySide6.QtGui import QAction, QPixmap
from PySide6.QtWidgets import QWidget, QGraphicsScene, QGraphicsPixmapItem

from include.image_button import ImageButton

class SelectScene(QGraphicsScene):
    def __init__(self, parent : QObject | None = None):
        super().__init__(parent)

        self.load_resource()
        self.setup_ui()
        self.connect_signal_and_slot()
    

    ################################
    ### Scene UI Setup           ###
    ################################
    
    def setup_ui(self):
        self.item_background = self.addPixmap(self.pixmap_background)
        self.item_background.setZValue(-1)

        self.item_button_story_mode  = ImageButton(self.pixmap_button_story_mode)
        self.item_button_story_mode.setPos(150, 230)
        self.addItem(self.item_button_story_mode)

        self.item_button_challenge = ImageButton(self.pixmap_button_challenge)
        self.item_button_challenge.setPos(150, 340)
        self.addItem(self.item_button_challenge)

        self.item_button_time_attack = ImageButton(self.pixmap_button_time_attack)
        self.item_button_time_attack.setPos(150, 450)
        self.addItem(self.item_button_time_attack)

        self.item_text_select_mode = self.addPixmap(self.pixmap_text_select_mode)
        self.item_text_select_mode.setPos(100, 100)

    ### Image Loader
    def load_resource(self):
        _image_root = os.path.join(os.path.dirname(__file__), '../image')

        self.pixmap_background = QPixmap(os.path.join(_image_root, 'backgrounds/TEMP_Select_Scene_BG.jpg'))

        self.pixmap_button_story_mode  = QPixmap(os.path.join(_image_root, 'buttons/button-select_story_mode.png'))
        self.pixmap_button_challenge   = QPixmap(os.path.join(_image_root, 'buttons/button-select_challenge.png'))
        self.pixmap_button_time_attack = QPixmap(os.path.join(_image_root, 'buttons/button-select_time_attack.png'))

        self.pixmap_text_select_mode = QPixmap(os.path.join(_image_root, 'misc/Select-Mode-Text.png'))
    
    ### Signal-Slot Connector
    def connect_signal_and_slot(self):
        pass