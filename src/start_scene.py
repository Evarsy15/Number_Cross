import os
from PySide6.QtCore import Qt, QObject, QRect, QRectF, Signal, Slot
from PySide6.QtGui import QAction, QPixmap
from PySide6.QtWidgets import QWidget, QGraphicsScene, QGraphicsPixmapItem

from include.image_button import ImageButton

class StartScene(QGraphicsScene):
    def __init__(self, parent : QObject | None = None):
        super().__init__(parent)
        self.setObjectName('Scene_#0_Start_Window')

        self.load_resource()
        self.setup_ui()
        self.connect_signal_and_slot()
    
    ###################################
    ### Signals and Slots
    ###################################

    startClicked  = Signal()
    howtoClicked  = Signal()
    optionClicked = Signal()

    def startButtonClickedHandler(self):
        self.startClicked.emit()

    def howtoplayButtonClickedHandler(self):
        self.howtoClicked.emit()
    
    def optionsButtonClickedHandler(self):
        self.optionClicked.emit()

    def setup_ui(self):
        self.item_background = self.addPixmap(self.pixmap_background)
        self.item_background.setZValue(-1)

        self.item_button_start  = ImageButton(self.pixmap_button_start)
        self.item_button_start.setPos(540, 480)
        self.addItem(self.item_button_start)

        self.item_button_how_to = ImageButton(self.pixmap_button_how_to)
        self.item_button_how_to.setPos(540, 550)
        self.addItem(self.item_button_how_to)

        self.item_button_option = ImageButton(self.pixmap_button_option)
        self.item_button_option.setPos(540, 620)
        self.addItem(self.item_button_option)

        self.item_authorizer = self.addPixmap(self.pixmap_authorizer)
        self.item_authorizer.setPos(520, 690)

    ### Image Loader
    def load_resource(self):
        _image_root = os.path.join(os.path.dirname(__file__), '../image')

        self.pixmap_background = QPixmap(os.path.join(_image_root, 'backgrounds/TEMP_bg_start_scene.jpg'))

        self.pixmap_button_start  = QPixmap(os.path.join(_image_root, 'buttons/button_start.png'))
        self.pixmap_button_how_to = QPixmap(os.path.join(_image_root, 'buttons/button_how_to.png'))
        self.pixmap_button_option = QPixmap(os.path.join(_image_root, 'buttons/button_options.png'))

        self.pixmap_authorizer = QPixmap(os.path.join(_image_root, 'misc/authorize.png'))
    
    ### Signal-Slot Connector
    def connect_signal_and_slot(self):
        self.item_button_start.buttonClicked.connect(self.startButtonClickedHandler)
        self.item_button_how_to.buttonClicked.connect(self.howtoplayButtonClickedHandler)
        self.item_button_option.buttonClicked.connect(self.optionsButtonClickedHandler)