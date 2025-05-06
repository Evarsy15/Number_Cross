import os
from PySide6.QtCore import Qt, QObject, QRect, QRectF, Signal, Slot
from PySide6.QtGui import QAction, QPixmap
from PySide6.QtWidgets import QWidget, QGraphicsScene, QGraphicsPixmapItem

class OptionsScene(QGraphicsScene):
    def __init__(self, parent : QObject | None = None):
        super().__init__(parent)