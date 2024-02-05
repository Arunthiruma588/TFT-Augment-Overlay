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
            # self.table.updateFirstAugmentStats(self.augmentName, self.augmentPlacement)
            # self.table.setItem(0,0, QTableWidgetItem(self.augmentName))
            # self.table.setItem(0,1, QTableWidgetItem(self.augmentPlacement))

            # # Data update 
            # self.table.update()
            # # Visible change
            # self.table.repaint()
            # print(self.table.itemAt(0,0).text())
            # print(self.table.itemAt(0,1).text())
            self.finished.emit()
        elif self.index == 2:
            self.table.setItem(1,0, QTableWidgetItem(self.augmentName))
            self.table.setItem(1,1, QTableWidgetItem(self.augmentPlacement))

            # Data update 
            self.table.update()
            # Visible change
            self.table.repaint()

            # print(self.table.itemAt(1,0))
            # print(self.table.itemAt(1,1))

            self.finished.emit()
        elif self.index == 3:
            self.table.setItem(2,0, QTableWidgetItem(self.augmentName))
            self.table.setItem(2,1, QTableWidgetItem(self.augmentPlacement))

            # Data update 
            self.table.update()
            # Visible change
            self.table.repaint()

            # print(self.table.itemAt(2,0))
            # print(self.table.itemAt(2,1))

            self.finished.emit()


class CreateTable(QTableWidget):
    finished = QtCore.pyqtSignal()

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
        # self.setAttribute(QtCore.Qt.WidgetAttribute.WA_DeleteOnClose, on=True)

        #Sets vertical and horizontal header to not visible (it just clutters UI)

        self.verticalHeader().setVisible(False);
        self.horizontalHeader().setVisible(False);


    def __insertFirstAugmentStats(self, augmentName, augmentPlacement):
        # Sets augmentName and augmentPlacement to the first row in table
        self.setItem(0,0, QTableWidgetItem(augmentName))
        self.setItem(0,1, QTableWidgetItem(augmentPlacement))
        # self.update()
        # self.repaint()
    def __insertSecondAugmentStats(self, augmentName, augmentPlacement):
        # Sets augmentName and augmentPlacement to the second row in table
        self.setItem(1,0, QTableWidgetItem(augmentName))
        self.setItem(1,1, QTableWidgetItem(augmentPlacement))
        # self.update()
        # self.repaint()
    def __insertThirdAugmentStats(self, augmentName, augmentPlacement):
        # Sets augmentName and augmentPlacement to the third row in table
        self.setItem(2,0, QTableWidgetItem(augmentName))
        self.setItem(2,1, QTableWidgetItem(augmentPlacement))
        # self.update()
        # self.repaint()
    def updateFirstAugmentStats(self, augmentName, augmentPlacement):
        self.setItem(0,0, QTableWidgetItem(augmentName))
        self.setItem(0,1, QTableWidgetItem(augmentPlacement))

        # Data update 
        # self.update()
        # # Visible change
        self.repaint()
    def updateSecondAugmentStats(self, augmentName, augmentPlacement):
        self.setItem(1,0, QTableWidgetItem(augmentName))
        self.setItem(1,1, QTableWidgetItem(augmentPlacement))

        # Data update 
        # self.update()
        # # Visible change
        self.repaint()
    def updateThirdAugmentStats(self, augmentName, augmentPlacement):
        self.setItem(2,0, QTableWidgetItem(augmentName))
        self.setItem(2,1, QTableWidgetItem(augmentPlacement))

        # Data update 
        # self.update()
        # # Visible change
        self.repaint()
    # def closeEvent(self, event):
    #     print("reaches the close event")
    #     event.ignore()
    #     self.finished.emit()
    # def showEvent(self, event):
    #     print(event.spontaneous())
    #     # event.accept()
    #     self.repaint()

class CreateMainWindow(QMainWindow):
    def __init__(self, data, stageNumber, resolution_x, resolution_y):
        QMainWindow.__init__(self)

        # if(resolution_x == 1920 and resolution_y == 1080):
        #     self.setGeometry(0, 657, int(resolution_x * 0.17), int(resolution_y * 0.16666))
        #     # Sets a fixed window size same as the assigned values to 
        #     self.setFixedSize(int(resolution_x * 0.17), int(resolution_y * 0.16666))
        # elif(resolution_x == 3840 and resolution_y == 2160):
        #     self.setGeometry(0, 650, int(resolution_x * 0.28), int(resolution_y * 0.16666))
        #     # self.setFixedSize(int(resolution_x * 0.28), int(resolution_y * 0.16666))

        # # Name of the window based on the stageNumber given
        # placeholder = ""
        # if stageNumber == 2:
        #     placeholder = "2-1"
        # elif stageNumber == 3:
        #     placeholder = "3-2"
        # elif stageNumber == 4:
        #     placeholder = "4-2"

        # self.setWindowTitle("Augment Stats at " + placeholder + "")

        # # Set priority over other windows
        # self.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint, on=True)

        # self.setAttribute(QtCore.Qt.WidgetAttribute.WA_AlwaysStackOnTop, on=True)

        # # # Makes sure window closes on Quit
        # self.setAttribute(QtCore.Qt.WidgetAttribute.WA_QuitOnClose, on=True)

        self.x = resolution_x
        self.y = resolution_y
        self.stageNumber = stageNumber
        self.table = CreateTable(data, stageNumber, resolution_x, resolution_y)
        # self.setCentralWidget(self.table)
        self.table.setVisible(True)
        # self.show()
        self.table.finished.connect(self.tableClose)

    def updateFirstAugmentStats(self, augmentName, augmentPlacement):
        # Assigns new data to first row in table

        # Creates a QThread that updates the first Augment stats in the table
        # self.thread = QtCore.QThread()
        # self.worker = Worker(self.table, 1, augmentName, augmentPlacement)
        # # Step 4: Move worker to the thread
        # self.worker.moveToThread(self.thread)
        # # Step 5: Connect signals and slots
        # self.thread.started.connect(self.worker.run)
        # self.worker.finished.connect(self.thread.quit)
        # self.worker.finished.connect(self.thread.wait)
        # self.worker.finished.connect(self.worker.deleteLater)
        # self.thread.finished.connect(self.thread.deleteLater)

        # # self.worker.progress.connect(self.reportProgress)
        # # Step 6: Start the thread
        # self.thread.start()

        self.table.updateFirstAugmentStats(augmentName, augmentPlacement)
        # self.repaint()
        # self.update()
        # self.show()

        # self.table.setItem(0,0, QTableWidgetItem(augmentName))
        # self.table.setItem(0,1, QTableWidgetItem(augmentPlacement))

        # # Data update 
        # self.table.update()
        # # Visible change
        # self.table.repaint()
        # self.update()
        # self.repaint()


    def updateSecondAugmentStats(self, augmentName, augmentPlacement):
        # self.thread = QtCore.QThread()
        # self.worker = Worker(self.table, 2, augmentName, augmentPlacement)
        # # Step 4: Move worker to the thread
        # self.worker.moveToThread(self.thread)
        # # Step 5: Connect signals and slots
        # self.thread.started.connect(self.worker.run)
        # self.worker.finished.connect(self.thread.quit)
        # self.worker.finished.connect(self.thread.wait)
        # self.worker.finished.connect(self.worker.deleteLater)
        # self.thread.finished.connect(self.thread.deleteLater)
        # # self.worker.progress.connect(self.reportProgress)
        # # Step 6: Start the thread
        # self.thread.start()
        # self.table.setItem(1,0, QTableWidgetItem(augmentName))
        # self.table.setItem(1,1, QTableWidgetItem(augmentPlacement))

        self.table.updateSecondAugmentStats(augmentName, augmentPlacement)

        # # Data update 
        # self.update()
        # # Visible change
        # self.repaint()

    def updateThirdAugmentStats(self, augmentName, augmentPlacement):
        # self.thread = QtCore.QThread()
        # self.worker = Worker(self.table, 3, augmentName, augmentPlacement)
        # # Step 4: Move worker to the thread
        # self.worker.moveToThread(self.thread)
        # # Step 5: Connect signals and slots
        # self.thread.started.connect(self.worker.run)
        # self.worker.finished.connect(self.thread.quit)
        # self.worker.finished.connect(self.thread.wait)
        # self.worker.finished.connect(self.worker.deleteLater)
        # self.thread.finished.connect(self.thread.deleteLater)
        # # self.worker.progress.connect(self.reportProgress)
        # # Step 6: Start the thread
        # self.thread.start()

        self.table.updateThirdAugmentStats(augmentName, augmentPlacement)
        
        # self.table.setItem(2,0, QTableWidgetItem(augmentName))
        # self.table.setItem(2,1, QTableWidgetItem(augmentPlacement))

        # # Data update 
        # self.update()
        # # Visible change
        # self.repaint()
    # def updateTable(self, data, stageNumber, resolution_x, resolution_y):
    #     if self.table is None:
    #         self.table = CreateTable(data, stageNumber, resolution_x, resolution_y)
    #         # self.setCentralWidget(self.table)
    #         # self.table.repaint()
    #         self.table.show()
    #     else:
    #         self.updateFirstAugmentStats(data[0][0], data[0][1])
    #         self.updateSecondAugmentStats(data[1][0], data[1][1])
    #         self.updateThirdAugmentStats(data[2][0], data[2][1])
    #         print(self.table.item(0,0).text())
    #         self.show()
    #         self.table.show()
            
            
        # self.show()
        print("enters into updateTable")
        

    def tableClose(self):
        print("reaches inside the tableClose event")
        data = [
            ["",""],
            ["",""],
            ["",""],
        ]
        self.updateFirstAugmentStats(data[0][0], data[0][1])
        self.updateSecondAugmentStats(data[1][0], data[1][1])
        self.updateThirdAugmentStats(data[2][0], data[2][1])
        # self.setCentralWidget(self.table)
        self.table.showMinimized()
    def tableOpen(self, data):
        if(self.x == 1920 and self.y == 1080):
            self.table.setGeometry(0, 657, int(self.x * 0.17), int(self.y * 0.16666))
        elif(self.x == 3840 and self.y == 2160):
            self.table.setGeometry(0, 650, int(self.x * 0.28), int(self.y * 0.16666))

        # Sets a fixed window size same as the assigned values to 
        self.table.setFixedSize(int(self.x * 0.17), int(self.y * 0.16666))

        self.table.showMaximized()
        self.updateFirstAugmentStats(data[0][0], data[0][1])
        self.updateSecondAugmentStats(data[1][0], data[1][1])
        self.updateThirdAugmentStats(data[2][0], data[2][1])