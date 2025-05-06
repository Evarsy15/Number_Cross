import os
from PySide6.QtCore import Qt, QObject, QRect, QRectF, Signal, Slot
from PySide6.QtGui import QAction, QPixmap
from PySide6.QtWidgets import QWidget, QGraphicsScene, QGraphicsPixmapItem

class StoryScene(QGraphicsScene):
    def __init__(self):
        super().__init__()
        