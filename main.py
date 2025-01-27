'''
    main.py

    Author : Nix
        e-mail : rabbitnix@postech.ac.kr
        github : https://github.com/Evarsy15
'''

import sys
from PySide6.QtWidgets import QApplication
from src.number_cross import NumberCross

if __name__ == '__main__':
    app = QApplication(sys.argv)
    prog = NumberCross()
    prog.show()
    sys.exit(app.exec())