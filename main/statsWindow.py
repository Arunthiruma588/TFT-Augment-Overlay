# Referenced from https://coderslegacy.com/python/pyqt6-qtablewidget-example/
# and https://stackoverflow.com/questions/25950049/creating-a-transparent-overlay-with-qt
# and https://realpython.com/python-pyqt-qthread/
from PyQt6 import QtCore, QtGui
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QMainWindow
import time


class Worker(QtCore.QObject):
    finished = QtCore.pyqtSignal()

    def __init__(self, table, index, augmentName, augmentPlacement):
        QtCore.QObject.__init__(self)
        self.table = table
        self.augmentName = augmentName
        self.augmentPlacement = augmentPlacement
        self.index = index

    def run(self):
        if self.index == 1:
            self.table.setItem(0,0, QTableWidgetItem(self.augmentName))
            self.table.setItem(0,1, QTableWidgetItem(self.augmentPlacement))

            # Data update 
            self.table.update()
            # # Visible change
            self.table.repaint()

            print(self.table.itemAt(0,0))
            print(self.table.itemAt(0,1))

            self.finished.emit()
        elif self.index == 2:
            self.table.setItem(1,0, QTableWidgetItem(self.augmentName))
            self.table.setItem(1,1, QTableWidgetItem(self.augmentPlacement))

            # Data update 
            self.table.update()
            # Visible change
            self.table.repaint()
            self.finished.emit()
        elif self.index == 3:
            self.table.setItem(2,0, QTableWidgetItem(self.augmentName))
            self.table.setItem(2,1, QTableWidgetItem(self.augmentPlacement))

            # Data update 
            self.table.update()
            # Visible change
            self.table.repaint()
            self.finished.emit()


class CreateTable(QTableWidget):
    def __init__(self, data, stageNumber, resolution_x, resolution_y):
        QTableWidget.__init__(self)
        self.setRowCount(3)
        self.setColumnCount(2)

        # Don't think we need layout, so trying to just show table

        # self.vBox = QVBoxLayout()
        # # self.vBox.addWidget(self)
        # self.setLayout(self.vBox)

        self.setColumnWidth(0, 1000)
        self.setColumnWidth(1, 300)

        self.setRowHeight(0, 60)
        self.setRowHeight(1, 60)
        self.setRowHeight(2, 60)

        self.__insertFirstAugmentStats(data[0][0], data[0][1])
        self.__insertSecondAugmentStats(data[1][0], data[1][1])
        self.__insertThirdAugmentStats(data[2][0], data[2][1])

        # # Name of the window based on the stageNumber given
        # placeholder = ""
        # if stageNumber == 2:
        #     placeholder = "2-1"
        # elif stageNumber == 3:
        #     placeholder = "3-2"
        # elif stageNumber == 4:
        #     placeholder = "4-2"

        # self.setWindowTitle("Augment Stats at " + placeholder + "")

        # Set priority over other windows
        # self.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint, on=True)
        # # Frameless window
        # # self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint, on=True)
        # # No Hints
        # # self.setWindowFlag(QtCore.Qt.WindowType.BypassWindowManagerHint, on=True)
        # self.setAttribute(QtCore.Qt.WidgetAttribute.WA_AlwaysStackOnTop, on=True)

        # # Makes sure window closes on Quit
        # self.setAttribute(QtCore.Qt.WidgetAttribute.WA_QuitOnClose, on=True)
        # Sets geometry of the window 
        # referenced from: https://stackoverflow.com/questions/25950049/creating-a-transparent-overlay-with-qt
        # QtWidgets.QStyle.alignedRect(
            #     QtCore.Qt.LayoutDirection.LeftToRight, QtCore.Qt.AlignmentFlag.AlignCenter,
            #     #Dimensions of your screen (subject to change)
            #     QtCore.QSize(int(resolution_x * 0.28), int(resolution_y * 0.16666)),
            #     #Position on the screen (you can move if you want)
            #     # QtCore.QSize(self.centralWidget.availableGeometry()),
            #     QtGui.QGuiApplication.primaryScreen().availableGeometry()
            # )
        # This sets the x, y, width, height of window based on resolution 
        # x and y refer to 0, 657 for example which are the starting coordinates on screen when the window is created
        # width, height refer to the window dimensions when created
        # (feel free to change this to preference)

        if(resolution_x == 1920 and resolution_y == 1080):
            self.setGeometry(0, 657, int(resolution_x * 0.17), int(resolution_y * 0.16666))
        elif(resolution_x == 3840 and resolution_y == 2160):
            self.setGeometry(0, 650, int(resolution_x * 0.28), int(resolution_y * 0.16666))

        # Sets a fixed window size same as the assigned values to 
        self.setFixedSize(int(resolution_x * 0.17), int(resolution_y * 0.16666))

        #Sets vertical and horizontal header to not visible (it just clutters UI)

        self.verticalHeader().setVisible(False);
        self.horizontalHeader().setVisible(False);
        # self.show()


    def __insertFirstAugmentStats(self, augmentName, augmentPlacement):
        # Sets augmentName and augmentPlacement to the first row in table
        self.setItem(0,0, QTableWidgetItem(augmentName))
        self.setItem(0,1, QTableWidgetItem(augmentPlacement))

    def __insertSecondAugmentStats(self, augmentName, augmentPlacement):
        # Sets augmentName and augmentPlacement to the second row in table
        self.setItem(1,0, QTableWidgetItem(augmentName))
        self.setItem(1,1, QTableWidgetItem(augmentPlacement))

    def __insertThirdAugmentStats(self, augmentName, augmentPlacement):
        # Sets augmentName and augmentPlacement to the third row in table
        self.setItem(2,0, QTableWidgetItem(augmentName))
        self.setItem(2,1, QTableWidgetItem(augmentPlacement))

    # Update functions for rerolls of augments

    # def updateFirstAugmentStats(self, augmentName, augmentPlacement):
    #     # # Assigns new data to first row in table
    #     self.setItem(0,0, QTableWidgetItem(augmentName))
    #     self.setItem(0,1, QTableWidgetItem(augmentPlacement))

    #     # Data update 
    #     self.update()
    #     # # Visible change
    #     self.repaint()

    #     # time.sleep(4)
    #     # self.thread = QtCore.QThread()
    #     # self.worker = Worker()
    #     # # Step 4: Move worker to the thread
    #     # self.worker.moveToThread(self.thread)
    #     # # Step 5: Connect signals and slots
    #     # self.thread.started.connect(self.worker.runFirstAugmentUpdate(self.itemAt(0,0), self.itemAt(0,1), augmentName=augmentName, augmentPlacement=augmentPlacement))
    #     # self.worker.finished.connect(self.thread.quit)
    #     # self.worker.finished.connect(self.worker.deleteLater)
    #     # self.thread.finished.connect(self.thread.deleteLater)
    #     # # self.worker.progress.connect(self.reportProgress)
    #     # # Step 6: Start the thread
    #     # self.thread.start()


    # def updateSecondAugmentStats(self, augmentName, augmentPlacement):
    #     # Assigns new data to second row in table
    #     # self.setItem(1,0, QTableWidgetItem(augmentName))
    #     # self.setItem(1,1, QTableWidgetItem(augmentPlacement))

    #     # # Data update
    #     # self.update()
    #     # # Visible change
    #     # self.repaint()
    #     self.thread = QtCore.QThread()
    #     self.worker = Worker()
    #     # Step 4: Move worker to the thread
    #     self.worker.moveToThread(self.thread)
    #     # Step 5: Connect signals and slots
    #     self.thread.started.connect(self.worker.runSecondAugmentUpdate(table=self, augmentName=augmentName, augmentPlacement=augmentPlacement))
    #     self.worker.finished.connect(self.thread.quit)
    #     self.worker.finished.connect(self.worker.deleteLater)
    #     self.thread.finished.connect(self.thread.deleteLater)
    #     # self.worker.progress.connect(self.reportProgress)
    #     # Step 6: Start the thread
    #     self.thread.start()

    # def updateThirdAugmentStats(self, augmentName, augmentPlacement):
    #     # Sets items to third row in table
    #     # self.setItem(2,0, QTableWidgetItem(augmentName))
    #     # self.setItem(2,1, QTableWidgetItem(augmentPlacement))

    #     # # Data update
    #     # self.update()
    #     # # Visible change
    #     # self.repaint()
    #     self.thread = QtCore.QThread()
    #     self.worker = Worker()
    #     # Step 4: Move worker to the thread
    #     self.worker.moveToThread(self.thread)
    #     # Step 5: Connect signals and slots
    #     self.thread.started.connect(self.worker.runThirdAugmentUpdate(table=self, augmentName=augmentName, augmentPlacement=augmentPlacement))
    #     self.worker.finished.connect(self.thread.quit)
    #     self.worker.finished.connect(self.worker.deleteLater)
    #     self.thread.finished.connect(self.thread.deleteLater)
    #     # self.worker.progress.connect(self.reportProgress)
    #     # Step 6: Start the thread
    #     self.thread.start()

    # def QCloseEvent(self):
    #     QApplication.quit()
    # def mouseEvent(self):
    #     QApplication.quit()

class CreateMainWindow(QMainWindow):
    def __init__(self, data, stageNumber, resolution_x, resolution_y):
        QMainWindow.__init__(self)

        if(resolution_x == 1920 and resolution_y == 1080):
            self.setGeometry(0, 657, int(resolution_x * 0.17), int(resolution_y * 0.16666))
            # Sets a fixed window size same as the assigned values to 
            self.setFixedSize(int(resolution_x * 0.17), int(resolution_y * 0.16666))
        elif(resolution_x == 3840 and resolution_y == 2160):
            self.setGeometry(0, 650, int(resolution_x * 0.28), int(resolution_y * 0.16666))
            # self.setFixedSize(int(resolution_x * 0.28), int(resolution_y * 0.16666))

        # Name of the window based on the stageNumber given
        placeholder = ""
        if stageNumber == 2:
            placeholder = "2-1"
        elif stageNumber == 3:
            placeholder = "3-2"
        elif stageNumber == 4:
            placeholder = "4-2"

        self.setWindowTitle("Augment Stats at " + placeholder + "")

        # Set priority over other windows
        self.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint, on=True)

        # self.setAttribute(QtCore.Qt.WidgetAttribute.WA_AlwaysStackOnTop, on=True)

        # Makes sure window closes on Quit
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_QuitOnClose, on=True)

        self.table = CreateTable(data, stageNumber, resolution_x, resolution_y)
        self.setCentralWidget(self.table)
        self.show()

    def updateFirstAugmentStats(self, augmentName, augmentPlacement):
        # # Assigns new data to first row in table

        # Creates a QThread that updates the first Augment stats in the table
        self.thread = QtCore.QThread()
        self.worker = Worker(self.table, 1, augmentName, augmentPlacement)
        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.thread.wait)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        # self.worker.progress.connect(self.reportProgress)
        # Step 6: Start the thread
        self.thread.start()


    def updateSecondAugmentStats(self, augmentName, augmentPlacement):
        self.thread = QtCore.QThread()
        self.worker = Worker(self.table, 2, augmentName, augmentPlacement)
        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.thread.wait)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        # self.worker.progress.connect(self.reportProgress)
        # Step 6: Start the thread
        self.thread.start()

    def updateThirdAugmentStats(self, augmentName, augmentPlacement):
        self.thread = QtCore.QThread()
        self.worker = Worker(self.table, 3, augmentName, augmentPlacement)
        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.thread.wait)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        # self.worker.progress.connect(self.reportProgress)
        # Step 6: Start the thread
        self.thread.start()

    def QCloseEvent(self):
        QApplication.quit()
    def mouseEvent(self):
        QApplication.quit()




# Testing purposes (moved to main.py)

# app = QApplication([])

# # app.setStyleSheet("""
# #     QLabel {
# #         margin: 0px;
# #         padding: 0px;
# #         font-size: 20px;
# #         color: "yellow";
# #     }
# # """)

# data = [
#           ["Jeweled Lotus II", "4.43"],
#           ["Healing Orbs II", "4.53"],
#           ["Last Stand", "4.65"],
#     ]

# window = CreateTable(data, 3, 1920, 1080)

# window.show()

# time.sleep(10)

# newData = [
#     ["Submit to the Pit", "4.76"],
#     ["You Have My Bow", "4.55"],
# ]

# window.updateFirstAugmentStats(newData[0][0], newData[0][1])
# # window.updateSecondAugmentStats(data[1][0], data[1][1])
# window.updateThirdAugmentStats(newData[1][0], newData[1][1])
# # window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# sys.exit(app.exec())