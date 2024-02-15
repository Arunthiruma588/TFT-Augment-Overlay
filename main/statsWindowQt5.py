from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QMainWindow, QPushButton
import time

class CreateTable(QTableWidget):
    finished = QtCore.pyqtSignal()

    def __init__(self, parent, data, stageNumber, resolution_x, resolution_y):
        super(QTableWidget, self).__init__(parent)
        self.setRowCount(3)
        self.setColumnCount(2)

        # self.setColumnWidth(0, 200)
        # self.setColumnWidth(1, 200)
        self.setColumnWidth(0, 150)
        self.setColumnWidth(1, 120)

        # self.setRowHeight(0, 60)
        # self.setRowHeight(1, 60)
        # self.setRowHeight(2, 60)

        self.setRowHeight(0, 50)
        self.setRowHeight(1, 50)
        self.setRowHeight(2, 50)

        self.__insertFirstAugmentStats(data[0][0], data[0][1])
        self.__insertSecondAugmentStats(data[1][0], data[1][1])
        self.__insertThirdAugmentStats(data[2][0], data[2][1])

        # This sets the x, y, width, height of window based on resolution 
        # x and y refer to 0, 657 for example which are the starting coordinates on screen when the window is created
        # width, height refer to the window dimensions when created
        # (feel free to change this to preference)

        # if(resolution_x == 1920 and resolution_y == 1080):
        #     # self.setGeometry(0, 870, int(resolution_x * 1), int(resolution_y * 0.1))
        #     self.setGeometry(0, 850, int(resolution_x * 0.25), int(resolution_y * 0.18))
        # elif(resolution_x == 3840 and resolution_y == 2160):
        #     self.setGeometry(0, 650, int(resolution_x * 0.28), int(resolution_y * 0.16666))

        # # Sets a fixed window size same as the assigned values to 
        # self.setFixedSize(int(resolution_x * 0.25), int(resolution_y * 0.18))

        # self.resize(int(resolution_x * 0.22), int(resolution_y * 0.18))
        self.resize(int(resolution_x * 0.22), int(resolution_y * 0.15))

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

        #Sets vertical and horizontal header to not visible (it just clutters UI)

        self.verticalHeader().setVisible(False);
        self.horizontalHeader().setVisible(False);


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
        
    def updateFirstAugmentStats(self, augmentName, augmentPlacement):
        self.setItem(0,0, QTableWidgetItem(augmentName))
        self.setItem(0,1, QTableWidgetItem(augmentPlacement))

        self.repaint()
        self.update()
    def updateSecondAugmentStats(self, augmentName, augmentPlacement):
        self.setItem(1,0, QTableWidgetItem(augmentName))
        self.setItem(1,1, QTableWidgetItem(augmentPlacement))

        self.repaint()
        self.update()
    def updateThirdAugmentStats(self, augmentName, augmentPlacement):
        self.setItem(2,0, QTableWidgetItem(augmentName))
        self.setItem(2,1, QTableWidgetItem(augmentPlacement))

        self.repaint()
        self.update()

class CreateMainWindow(QMainWindow):
    def __init__(self, data, stageNumber, resolution_x, resolution_y):
      QMainWindow.__init__(self)

      if(resolution_x == 1920 and resolution_y == 1080):
        # Before fitting into left-corner: self.setGeometry(0, 850, int(resolution_x * 0.20), int(resolution_y * 0.18))
        self.setGeometry(0, 880, int(resolution_x * 0.14), int(resolution_y * 0.16))
      elif(resolution_x == 3840 and resolution_y == 2160):
        self.setGeometry(0, 650, int(resolution_x * 0.28), int(resolution_y * 0.16666))

      # Sets a fixed window size same as the assigned values to 
      # self.setFixedSize(int(resolution_x * 0.25), int(resolution_y * 0.18))

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
    #   self.raise_()


      self.table = CreateTable(self, data, stageNumber, resolution_x, resolution_y)
      self.table.show()

      self.show()
      # self.x = resolution_x
      # self.y = resolution_y
      # self.stageNumber = stageNumber

    def updateTable(self, tag, stageNumber):
      if tag == "hide":
        placeholder = ""
        if stageNumber == 2:
            placeholder = "2-1"
        elif stageNumber == 3:
            placeholder = "3-2"
        elif stageNumber == 4:
            placeholder = "4-2"

        self.setWindowTitle("Augment Stats at " + placeholder + "")


        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_WState_Hidden)
        # self.setAttribute(QtCore.Qt.WidgetAttribute.WA)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_DontShowOnScreen, on=True)
        # self.hide()

        # self.table.setAttribute(QtCore.Qt.WidgetAttribute.WA_DontShowOnScreen, on=True)
      if tag == "show":

        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_WState_Visible)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_DontShowOnScreen, on=False)

        self.show()
        self.table.repaint()
        self.repaint()
        self.update()




    def updateFirstAugmentStats(self, augmentName, augmentPlacement):
      self.table.updateFirstAugmentStats(augmentName, augmentPlacement)
      self.repaint()
      self.update()

    def updateSecondAugmentStats(self, augmentName, augmentPlacement):
      self.table.updateSecondAugmentStats(augmentName, augmentPlacement)
      self.repaint()
      self.update()

    def updateThirdAugmentStats(self, augmentName, augmentPlacement):
      self.table.updateThirdAugmentStats(augmentName, augmentPlacement)
      self.repaint()
      self.update()
        # print("enters into updateTable")