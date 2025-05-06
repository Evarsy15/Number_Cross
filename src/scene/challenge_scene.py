import os
from PySide6.QtCore import Qt, QObject, QRect, QRectF, Signal, Slot
from PySide6.QtGui import QAction, QPixmap
from PySide6.QtWidgets import QWidget, QGraphicsScene, QGraphicsPixmapItem

class ChallengeMainScene(QGraphicsScene):
    def __init__(self):
        super().__init__()
        self.setObjectName('Scene_#3_Challenge_Main')
        self.setSceneRect(0, 0, 1280, 720)

        self.load_resource()
        self.setup_ui()
        self.connect_signal_and_slot()
    
    ### Image Loader
    def load_resource(self):
        _image_root = os.path.join(os.path.dirname(__file__), '../../image')

        self.pixmap_background = QPixmap(os.path.join(_image_root, 'backgrounds/TEMP_Challenge_Main_Scene_BG.jpg'))

        