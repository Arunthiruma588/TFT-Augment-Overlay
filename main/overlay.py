# Referenced from https://www.pythonguis.com/tutorials/pyqt6-creating-your-first-window/
# and https://stackoverflow.com/questions/25950049/creating-a-transparent-overlay-with-qt

import sys
from PyQt6 import QtCore, QtGui, uic
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout

# Referenced from https://coderslegacy.com/python/pyqt6-qtablewidget-example/

# class TableModel(QtCore.QAbstractItemModel):

#     # TableModelindex = None

#     def __init__(self, data):
#         super(TableModel, self).__init__()
#         self._data = data

#     def data(self, index, role):
#         if role == QtCore.Qt.ItemDataRole.DisplayRole:
#             # See below for the nested-list data structure.
#             # .row() indexes into the outer list,
#             # .column() indexes into the sub-list
#             # TableModelindex = index
#             return self._data[index.row()][index.column()]

#     def rowCount(self, index):
#         # The length of the outer list.
#         return len(self._data)

#     def columnCount(self, index):
#         # The following takes the first sub-list, and returns
#         # the length (only works if all rows are an equal length)
#         return len(self._data[0])

class MainWindow(QMainWindow):

    resolution_x = None
    resolution_y = None

    def __init__(self, data, resolution_x, resolution_y):
        QMainWindow.__init__(self)
        self.setWindowTitle("AugmentStatsOverlay")
        augmentTable = CreateTable()
        augmentTable.insertFirstAugmentStats(data[0][0], data[0][1])
        augmentTable.insertSecondAugmentStats(data[1][0], data[1][1])
        augmentTable.insertThirdAugmentStats(data[2][0], data[2][1])
        self.setCentralWidget(augmentTable)


        # header = self.table.horizontalHeader()       
        # header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.Stretch)
        # header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        # header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        # self.resolution_x = resolution_x
        # self.resolution_y = resolution_y
        # # Name of Overlay Application
        # # Makes sure it's above all other windows
        # self.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint, on=False)
        # # Frameless window
        # self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint, on=False)
        # # No Hints 
        # self.setWindowFlag(QtCore.Qt.WindowType.BypassWindowManagerHint, on=False)
        # # Size and direction of window configuration
        self.setGeometry(
            QtWidgets.QStyle.alignedRect(
                QtCore.Qt.LayoutDirection.LeftToRight, QtCore.Qt.AlignmentFlag.AlignCenter,
                #Dimensions of your screen (subject to change)
                QtCore.QSize(int(resolution_x * 0.30), int(resolution_y * 0.1999)),
                QtGui.QGuiApplication.primaryScreen().availableGeometry()
            )
        )


        # self.model = TableModel(data)
        # self.table.setModel(self.model)

        # self.setCentralWidget(self.table)
        # Translucent background
        # self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground, on=True)
        # self.setStyleSheet("background: transparent")

        # self.setAttribute(QtCore.Qt.WidgetAttribute.WA_AlwaysStackOnTop, on=True)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_ShowWithoutActivating, on=False)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_QuitOnClose, on=True)

        # self.setWindowOpacity(0);

    # Referenced from https://coderslegacy.com/python/pyqt6-qtablewidget-example/
    # def firstAugmentInput(self. augmentName, augmentPlacement):
    
    def QCloseEvent(self):
        QApplication.quit()
    def mouseEvent(self):
        QApplication.quit()

class CreateTable(QTableWidget):
    def __init__(self):
        QTableWidget.__init__(self)
        self.setRowCount(3)
        self.setColumnCount(2)

        self.vBox = QVBoxLayout()
        # self.vBox.addWidget(self)
        self.setLayout(self.vBox)

        self.setHorizontalHeaderLabels(["AugmentName", "Avg. Placement at 2-1"])
        self.setColumnWidth(0, 350)
        self.setColumnWidth(1, 200)

        self.setRowHeight(0, 60)
        self.setRowHeight(1, 60)
        self.setRowHeight(2, 60)

        # self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents, on=True)

    def insertFirstAugmentStats(self, augmentName, augmentPlacement):
        # self.label = QLabel("", self)
        # self.label.setText(augmentPlacement)
        #Subject to change 
        # self.label.move(640, 810) values for 1920x1080
        # self.label.move(int(self.resolution_x * (1/3)), int(self.resolution_y * 0.75))
        self.setItem(0,0, QTableWidgetItem(augmentName))
        self.setItem(0,1, QTableWidgetItem(augmentPlacement))

    def insertSecondAugmentStats(self, augmentName, augmentPlacement):
        # self.label = QLabel("", self)
        # self.label.setText(augmentPlacement)
        # # Subject to change 
        # # self.label.move(940, 810) values for 1920x1080
        # self.label.move(int(self.resolution_x * (47/96)), int(self.resolution_y * 0.75))
        self.setItem(1,0, QTableWidgetItem(augmentName))
        self.setItem(1,1, QTableWidgetItem(augmentPlacement))

    def insertThirdAugmentStats(self, augmentName, augmentPlacement):
        # self.label = QLabel("", self)
        # self.label.setText(augmentPlacement)
        # #Subject to change 
        # #self.label.move(1240, 810) values for 1920x1080
        # self.label.move(int(self.resolution_x * (31/48)), int(self.resolution_y * 0.75))
        self.setItem(2,0, QTableWidgetItem(augmentName))
        self.setItem(2,1, QTableWidgetItem(augmentPlacement))

app = QApplication([])

# app.setStyleSheet("""
#     QLabel {
#         margin: 0px;
#         padding: 0px;
#         font-size: 20px;
#         color: "yellow";
#     }
# """)

data = [
          ["Jeweled Lotus II", "4.43"],
          ["Healing Orbs II", "4.53"],
          ["Last Stand", "4.65"],
    ]

window = MainWindow(data, 1920, 1080)
# window.createFirstAugmentLabel("4.76")
# window.createSecondAugmentLabel("4.35")
# window.createThirdAugmentLabel("4.60")
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

sys.exit(app.exec())