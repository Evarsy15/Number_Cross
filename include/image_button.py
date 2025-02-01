'''
    image_button.py

    Author : Nix
        e-mail : rabbitnix@postech.ac.kr
        github : https://github.com/Evarsy15
'''

from enum import Enum
from PySide6.QtCore import Qt, QObject, Signal
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QGraphicsPixmapItem, QGraphicsItem

'''
    ImageButton provides image-based button available in QGraphicsScene,
    which is widely used in game application.
'''
class ImageButton(QObject, QGraphicsPixmapItem):
    
    buttonClicked = Signal()

    class ButtonMode(Enum):
        ActivateWhenPressed  = 0
        ActivateWhenReleased = 1

    def __init__(self, pixmap : QPixmap,
                       parent : QObject | None = None,
                       parentItem : QGraphicsItem | None = None):
        QObject.__init__(self, parent)
        QGraphicsPixmapItem.__init__(self, pixmap, parentItem)

        # Set Cursor | Default : PointingHandCursor
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        # Set Button Mode
        self.__button_mode = ImageButton.ButtonMode.ActivateWhenPressed

    def setButtonMode(self, buttonMode : ButtonMode) -> None:
        self.__button_mode = buttonMode
    
    def mousePressEvent(self, event):
        self.buttonClicked.emit()
    
    def mouseReleaseEvent(self, event):
        if self.__button_mode == ImageButton.ButtonMode.ActivateWhenPressed:
            return
    
