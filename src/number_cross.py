

from PySide6.QtCore import Qt, QObject, QRect, Signal, Slot
from PySide6.QtGui import QAction, QPixmap
from PySide6.QtWidgets import QWidget, QGraphicsScene, QGraphicsView

from src.start_scene import StartScene

class NumberCross(QGraphicsView):
    def __init__(self):
        super().__init__()

    ### Set basic properties
        # Invalidate scroll bar
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        # Set window size
        self.setFixedSize(1280, 720)
        self.setWindowTitle('Number Cross')

        # Set all scenes required
        self.start_scene = StartScene(QRect(0, 0, 1280, 720))

        # Set initial scene as StartScene
        self.setScene(self.start_scene)