import os
from PySide6.QtCore import Qt, QObject, QRect, QRectF, Signal, Slot
from PySide6.QtGui import QAction, QPixmap
from PySide6.QtWidgets import QWidget, QGraphicsScene, QGraphicsPixmapItem

class StartScene(QGraphicsScene):
    def __init__(self, parent : QObject | None = None):
        super().__init__(parent)

        self.pixmap_bg = QPixmap(os.path.join(os.path.dirname(__file__), 'TEMP_bg_start_scene.jpg'))
        self.item_bg = self.addPixmap(self.pixmap_bg)
        print(self.item_bg)