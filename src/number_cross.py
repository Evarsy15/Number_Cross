

from PySide6.QtCore import Qt, QObject, QRect, Signal, Slot
from PySide6.QtGui import QAction, QPixmap
from PySide6.QtWidgets import QWidget, QGraphicsScene, QGraphicsView

from include.settings import Settings

from src.start_scene  import StartScene
from src.select_scene import SelectScene

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

    ### Set all scenes required
        self.start_scene  = StartScene()
        self.select_scene = SelectScene()

        # Connect Signals to Slot
        self.connect_signal_and_slot()

        # Set initial scene as StartScene
        self.setScene(self.start_scene)
    
    ### Slots for Start Scene (Scene #0)
    def S0_startClickedHandler(self):
        print('Start Scene : startClickedHandler()')
        self.setScene(self.select_scene)

    
    def S0_howtoClickedHandler(self):
        print('Start Scene : howtoClickedHandler()')

    def S0_optionClickedHandler(self):
        print('Start Scene : optionClickedHandler()')

    ### Signal-Slot Connector
    def connect_signal_and_slot(self):
        # Scene 0 : Start Scene
        self.start_scene.startClicked.connect(self.S0_startClickedHandler)
        self.start_scene.howtoClicked.connect(self.S0_howtoClickedHandler)
        self.start_scene.optionClicked.connect(self.S0_optionClickedHandler)

        # Scene 0-1 : How-to-play Scene

        # Scene 0-2 : Options Setting Scene