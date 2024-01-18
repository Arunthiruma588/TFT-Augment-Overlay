# Referenced from https://www.pythonguis.com/tutorials/pyqt6-creating-your-first-window/
# and https://stackoverflow.com/questions/25950049/creating-a-transparent-overlay-with-qt

from PyQt6 import QtCore, QtGui, uic
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel

class MainWindow(QMainWindow):

    resolution_x = None
    resolution_y = None

    def __init__(self, resolution_x, resolution_y):
        QMainWindow.__init__(self)
        self.resolution_x = resolution_x
        self.resolution_y = resolution_y
        # Name of Overlay Application
        self.setWindowTitle("AugmentStatsOverlay")
        # Makes sure it's above all other windows
        self.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint, on=True)
        # Frameless window
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint, on=True)
        # No Hints 
        self.setWindowFlag(QtCore.Qt.WindowType.BypassWindowManagerHint, on=True)
        # Size and direction of window configuration
        self.setGeometry(
            QtWidgets.QStyle.alignedRect(
                QtCore.Qt.LayoutDirection.LeftToRight, QtCore.Qt.AlignmentFlag.AlignCenter,
                #Dimensions of your screen (subject to change)
                QtCore.QSize(resolution_x, resolution_y),
                QtGui.QGuiApplication.primaryScreen().availableGeometry()
            )
        )
        # Translucent background
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground, on=True)
        self.setStyleSheet("background: transparent")

        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_AlwaysStackOnTop, on=True)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents, on=True)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_ShowWithoutActivating, on=True)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_QuitOnClose, on=True)

        # Testing purposes (doesn't work)
        # self.setStyleSheet("background-image: ../test-img/FullScreenAugmentChoices.png;")

        # self.setWindowOpacity(0);
    
    # self.label.move(x, y coordinates)

    def createFirstAugmentLabel(self, augmentPlacement):
        self.label = QLabel("", self)
        self.label.setText(augmentPlacement)
        #Subject to change 
        # self.label.move(640, 810) values for 1920x1080
        self.label.move(int(self.resolution_x * (1/3)), int(self.resolution_y * 0.75))

    def createSecondAugmentLabel(self, augmentPlacement):
        self.label = QLabel("", self)
        self.label.setText(augmentPlacement)
        #Subject to change 
        # self.label.move(940, 810) values for 1920x1080
        self.label.move(int(self.resolution_x * (47/96)), int(self.resolution_y * 0.75))

    def createThirdAugmentLabel(self, augmentPlacement):
        self.label = QLabel("", self)
        self.label.setText(augmentPlacement)
        #Subject to change 
        #self.label.move(1240, 810) values for 1920x1080
        self.label.move(int(self.resolution_x * (31/48)), int(self.resolution_y * 0.75))

    def QCloseEvent(self):
        QApplication.quit()