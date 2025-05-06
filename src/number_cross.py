

from PySide6.QtCore import Qt, QObject, QRect, Signal, Slot
from PySide6.QtGui import QAction, QPixmap
from PySide6.QtWidgets import QWidget, QGraphicsScene, QGraphicsView

from include.settings import Settings

from src.scene.start_scene     import StartScene
from src.scene.select_scene    import SelectScene
from src.scene.challenge_scene import ChallengeMainScene

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
        # Scene #0
        self.start_scene  = StartScene()

        # Scene #1
        self.select_scene = SelectScene()

        # Scene #3
        self.challenge_scene = ChallengeMainScene()

        # Connect Signals to Slot
        self.connect_signal_and_slot()

        # Set initial scene as StartScene
        self.setScene(self.start_scene)

#########################################
### Slots
#########################################

### Slots for Start Scene (Scene #0)
    def S0_startClickedHandler(self):
        print('Start Scene : startClickedHandler()')
        self.setScene(self.select_scene)
    
    def S0_howtoClickedHandler(self):
        print('Start Scene : howtoClickedHandler()')

    def S0_optionClickedHandler(self):
        print('Start Scene : optionClickedHandler()')
    
### Slots for Select Scene (Scene #1)
    def S1_challengeClickedHandler(self):
        print('Select Scene : challengeClickedHandler()')

    def S1_gobackClickedHandler(self):
        self.setScene(self.start_scene)

#########################################
### Signal-Slot Connector
#########################################
    def connect_signal_and_slot(self):
        # Scene 0 : Start Scene
        self.start_scene.startClicked.connect(self.S0_startClickedHandler)
        self.start_scene.howtoClicked.connect(self.S0_howtoClickedHandler)
        self.start_scene.optionClicked.connect(self.S0_optionClickedHandler)

        # Scene 0-1 : How-to-play Scene

        # Scene 0-2 : Options Setting Scene

        # Scene 1 : Game Mode Select Scene
        self.select_scene.challengeClicked.connect(self.S1_challengeClickedHandler)
        self.select_scene.gobackClicked.connect(self.S1_gobackClickedHandler)